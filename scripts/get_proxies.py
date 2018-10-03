# from tables.proxies import proxies
import json
_DEFAULT_DICT = {'http': 'http://103.207.4.170:60570', 'https': 'https://103.207.4.170:60570',
                 'ftp_proxy': 'ftp://103.207.4.170:60570'}
_proxies = []
ips = open('tables/proxies.txt', 'r').readlines()
ports = open('tables/ports.txt', 'r').readlines()

ips = [ip.strip() for ip in ips]
ports = [port.strip() for port in ports]
for ip, port in zip(ips, ports):
    _proxies.append({'http': f'http://{ip}:{port}', 'https': f'https://{ip}:{port}',
                     'ftp_proxy': f'ftp://{ip}:{port}'})


with open('tables/proxies.json', 'w') as _input_file:
    json.dump(_proxies, _input_file)
# print(_proxies)
print(len(_proxies))
