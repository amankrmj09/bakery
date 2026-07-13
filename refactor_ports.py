import os
import re
import subprocess

ports_map = {
    'bakery_api_gateway': 8080,
    'config-server': 8081,
    'bakery_eureka_server': 8082,
    'bakery_auth_service': 8083,
    'bakery_cart_service': 8084,
    'bakery_notification_service': 8085,
    'bakery_order_service': 8086,
    'bakery_payment_service': 8087,
    'bakery_product_service': 8088
}

base_path = 'd:/dev_space/bakery'

# Step 1: Remove server.port from config-repo files
config_repo_path = os.path.join(base_path, 'config-repo')
for root, dirs, files in os.walk(config_repo_path):
    for file in files:
        if file.endswith('.yml') or file.endswith('.yaml'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r') as f:
                content = f.read()
            
            # Remove "server:\n  port: <number>" block if present
            # We must be careful not to remove other server properties if they exist, but usually it's just server.port
            # For this simple case, we can regex replace it.
            # Assuming format:
            # server:
            #   port: <num>
            new_content = re.sub(r'server:\s*\n\s*port:\s*\d+\n', '', content)
            
            if new_content != content:
                with open(filepath, 'w') as f:
                    f.write(new_content)
                print(f"Removed server.port from config-repo/{file}")

# Step 2-5: Update all services
for service, port in ports_map.items():
    service_dir = os.path.join(base_path, service)
    if not os.path.exists(service_dir):
        continue
    
    # 2. Update application.yml
    app_yml_path = os.path.join(service_dir, 'src', 'main', 'resources', 'application.yml')
    if os.path.exists(app_yml_path):
        with open(app_yml_path, 'r') as f:
            content = f.read()
        
        # Ensure server.port is in application.yml
        if 'server:' not in content:
            # Append it to the top or bottom
            content = f"server:\n  port: ${{SERVER_PORT:{port}}}\n" + content
        else:
            # If server: exists but no port:, add it
            if 'port:' not in content:
                content = content.replace('server:\n', f'server:\n  port: ${{SERVER_PORT:{port}}}\n')
        
        # Update configserver port to 8081
        content = re.sub(r'CONFIG_SERVER_URL:http://localhost:\d+', 'CONFIG_SERVER_URL:http://localhost:8081', content)
        
        with open(app_yml_path, 'w') as f:
            f.write(content)
            
    # 2b. Eureka application-dev.yml update
    if service == 'bakery_eureka_server':
        dev_yml_path = os.path.join(service_dir, 'src', 'main', 'resources', 'application-dev.yml')
        if os.path.exists(dev_yml_path):
            with open(dev_yml_path, 'r') as f:
                content = f.read()
            # replace 8761 with 8082
            content = content.replace('http://localhost:8761/eureka/', 'http://localhost:8082/eureka/')
            with open(dev_yml_path, 'w') as f:
                f.write(content)

    # 3. Update .env and .env.example
    for env_file in ['.env', '.env.example']:
        env_path = os.path.join(service_dir, env_file)
        if os.path.exists(env_path):
            with open(env_path, 'r') as f:
                content = f.read()
            
            # Add SERVER_PORT if missing
            if 'SERVER_PORT=' not in content:
                content += f"\nSERVER_PORT={port}\n"
            else:
                content = re.sub(r'SERVER_PORT=\d+', f'SERVER_PORT={port}', content)
            
            # Update CONFIG_SERVER_URL to 8081
            content = re.sub(r'CONFIG_SERVER_URL=http://config-server:\d+', 'CONFIG_SERVER_URL=http://config-server:8081', content)
            content = re.sub(r'CONFIG_SERVER_URL=http://localhost:\d+', 'CONFIG_SERVER_URL=http://localhost:8081', content)
            
            # Update EUREKA_URL to 8082
            content = re.sub(r'EUREKA_URL=http://eureka-server:\d+/eureka/', 'EUREKA_URL=http://eureka-server:8082/eureka/', content)
            content = re.sub(r'EUREKA_URL=http://localhost:\d+/eureka/', 'EUREKA_URL=http://localhost:8082/eureka/', content)
            
            with open(env_path, 'w') as f:
                f.write(content)

    # 4. Update Dockerfile
    dockerfile_path = os.path.join(service_dir, 'Dockerfile')
    if os.path.exists(dockerfile_path):
        with open(dockerfile_path, 'r') as f:
            lines = f.readlines()
            
        with open(dockerfile_path, 'w') as f:
            for line in lines:
                # Remove existing ENV SERVER_PORT if it was already injected
                if line.startswith('ENV SERVER_PORT='):
                    continue
                # Update EXPOSE
                if line.startswith('EXPOSE '):
                    f.write(f'EXPOSE {port}\n')
                    f.write(f'ENV SERVER_PORT={port}\n')
                else:
                    f.write(line)
                    
    print(f"Refactored {service}")
