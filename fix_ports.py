import os

ports_map = {
    'bakery_auth_service': 8082,
    'bakery_cart_service': 8085,
    'bakery_eureka_server': 8761,
    'bakery_notification_service': 8086,
    'bakery_order_service': 8084,
    'bakery_payment_service': 8087,
    'bakery_product_service': 8083,
    'config-server': 8021
}

base_path = 'd:/dev_space/bakery'

for service, port in ports_map.items():
    dockerfile_path = os.path.join(base_path, service, 'Dockerfile')
    
    if os.path.exists(dockerfile_path):
        with open(dockerfile_path, 'r') as f:
            lines = f.readlines()
            
        with open(dockerfile_path, 'w') as f:
            for line in lines:
                if line.startswith('EXPOSE 8080'):
                    f.write(f'EXPOSE {port}\n')
                else:
                    f.write(line)
        print(f'Updated {service} to EXPOSE {port}')

