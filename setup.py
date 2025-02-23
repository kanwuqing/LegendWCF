from setuptools import setup, Extension, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r', encoding='utf-8') as f:
    req = f.read().split('\n')

# for i in range(len(req)):
#     req[i] = req[i].split('==')[0]
# print(req)

setup(name='LegendWCF',  # 包名
    version='1.1.0',  # 版本号
    description='对于微信机器人编码体验的提升以及对WCFerry接口的优化',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='kanwuqing',
    author_email='kanwuqing@163.com',
    url='https://github.com/kanwuqing/LegendWCF',
    install_requires=req,
    license='MPL License',
    packages=find_packages(),
    platforms=["all"],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries'
    ],
)
