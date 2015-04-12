from fabric.api import *

def bootstrap():
    run('mkdir -p /var/www/hackathon')
    with cd('/var/www/hackathon'):
        run('virtualenv env')
        run('. env/bin/activate')
        put('config/hackathon.wsgi','hackathon.wsgi')
    put('config/hackathon.vhost.dev', '/etc/apache2/sites-available/hackathon.conf', use_sudo=True, mirror_local_mode=True)
    run('sudo a2ensite hackathon')

def pack():
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/hackathon.tar.gz')
    run('mkdir -p /tmp/hackathon')

    with cd('/tmp/hackathon'):
        run('tar xzf /tmp/hackathon.tar.gz')
        with cd('/tmp/hackathon/%s' % dist):
            run('/var/www/hackathon/env/bin/python setup.py install')
    run('rm -rf /tmp/hackathon /tmp/hackathon.tar.gz')
    run('sudo service apache2 reload')