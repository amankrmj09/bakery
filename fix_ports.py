import os
import re

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

for service, port in ports_map.items():
    service_dir = os.path.join(base_path, service)
    app_yml_path = os.path.join(service_dir, 'src', 'main', 'resources', 'application.yml')
    if os.path.exists(app_yml_path):
        with open(app_yml_path, 'r') as f:
            content = f.read()
            
        # Check if "server:" (standalone) is in the file
        if not re.search(r'^server:\s*$', content, re.MULTILINE):
            content = f"server:\n  port: ${{SERVER_PORT:{port}}}\n\n" + content
        else:
            if not re.search(r'^\s*port:\s*', content, re.MULTILINE):
                content = re.sub(r'(^server:\s*$)', rf'\1\n  port: ${{SERVER_PORT:{port}}}', content, flags=re.MULTILINE)
                
        with open(app_yml_path, 'w') as f:
            f.write(content)
            
    print(f"Fixed {service}")
