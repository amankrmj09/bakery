import os
import re

ports_map = {
    'config-server': 8081,
}

base_path = 'd:/dev_space/bakery'

for service, port in ports_map.items():
    service_dir = os.path.join(base_path, service)
    app_yml_path = os.path.join(service_dir, 'src', 'main', 'resources', 'application.yaml')
    if os.path.exists(app_yml_path):
        with open(app_yml_path, 'r') as f:
            content = f.read()
            
        if not re.search(r'^server:\s*$', content, re.MULTILINE):
            content = f"server:\n  port: ${{SERVER_PORT:{port}}}\n\n" + content
        else:
            if not re.search(r'^\s*port:\s*', content, re.MULTILINE):
                content = re.sub(r'(^server:\s*$)', rf'\1\n  port: ${{SERVER_PORT:{port}}}', content, flags=re.MULTILINE)
                
        with open(app_yml_path, 'w') as f:
            f.write(content)
            
    print(f"Fixed {service}")
