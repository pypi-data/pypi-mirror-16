import setuptools

version = '1.0.4'

setuptools.setup(
        name='ctec_thrift_client',
        version=version,
        packages=['ctec_thrift_client'],
        author='ZhangZhaoyuan',
        author_email='zhangzhy@chinatelecom.cn',
        url='http://www.189.cn',
        description='189 thrift rpc client',
        install_requires=['kazoo>=2.2.1', 'thriftpy>=0.3.5']
)