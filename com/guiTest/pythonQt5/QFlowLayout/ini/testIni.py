import configparser  # 引入模块


def create():
    config = configparser.ConfigParser()  # 类中一个方法 #实例化一个对象
    config["DEFAULT"] = {'ServerAliveInterval': '45',
                         'Compression': 'yes',
                         'CompressionLevel': '9',
                         'ForwardX11': 'yes'
                         }  # 类似于操作字典的形式
    config['bitbucket.org'] = {'User': 'Atlan'}  # 类似于操作字典的形式
    config['topsecret.server.com'] = {'Host Port': '50022', 'ForwardX11': 'no'}
    config.write(open('example.ini', 'w'))  # 将对象写入文件


def read():
    config = configparser.ConfigParser()
    # ---------------------------查找文件内容,基于字典的形式
    print(config.sections())  # []
    config.read('example.ini')
    print(config.sections())  # ['bitbucket.org', 'topsecret.server.com']
    print('bytebong.com' in config)  # False
    print('bitbucket.org' in config)  # True
    print(config['bitbucket.org']["user"])  # Atlan
    print(config['DEFAULT']['Compression'])  # yes
    print(config['topsecret.server.com']['ForwardX11'])  # no
    print(config['bitbucket.org'])  # <Section: bitbucket.org>
    for key in config['bitbucket.org']:  # 注意,有default会默认default的键
        print(key)
    print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
    print(config.items('bitbucket.org'))  # 找到'bitbucket.org'下所有键值对
    print(config.get('bitbucket.org', 'compression'))  # yes       get方法Section下的key对应的value

def update():
    config = configparser.ConfigParser()
    config.read('example.ini')  # 读文件
    config.add_section('yuan')  # 添加section
    config.remove_section('bitbucket.org')  # 删除section
    config.remove_option('topsecret.server.com', "forwardx11")  # 删除一个配置想
    config.set('topsecret.server.com', 'k1', '11111')
    config.set('yuan', 'k2', '22222')
    config.write(open('new2.ini', 'w'))

if __name__ == "__main__":
    read()

