# Open Bacchus 
Open Bacchus Project is a backup solution for oVirt/RHEV-M environment. It is being developed based on Python 2.7, Django 1.10 and oVirt Python SDK 4.1. Please be aware that it is still under development.
Thank you for checking it out.

## Installation
### Prerequisites
Please install the following packages on to your favorite Linux distro.
- Python 2.7.x
- pip
- MariaDB
- RabbitMQ

### Installation Steps
1. Install django framework 1.10.x
..* pip install django==1.10.6

2. Install oVirt Python SDK
..* pip install ovirt-engine-sdk-python==4.1.2

3. Install Python MySQL support
..* pip install MySQL-python

4. Install Celery
..* pip install celery==4.0.2
..* pip install django-celery-beat
..* pip install django-celery-results
..* pip install flower

5. Create bacchus database and user on MariaDB
..* create database bacchus;
..* grant all on bacchus.* to bacchus@localhost identified by 'bacchus';

6. Create bacchus user on RabbitMQ (run the following commands with root user)
..* # rabbitmqctl add_user bacchus bacchus
..* # rabbitmqctl add_vhost bacchus
..* # rabbitmqctl set_user_tags bacchus Administrator
..* # rabbitmqctl set_permissions -p bacchus bacchus ".*" ".*" ".*"

6. Create bacchus user and group on Linux
..* useradd bacchus

7. Login with bacchus user and get the Bacchus code from git repository
..* [bacchus@localhost]$ git clone https://github.com/openbacchus/bacchus.git

8. Create the Bacchus Database layout 
..* cd bacchus
..* python manage.py check
..* python manage.py migrate

9. Add your host into Django settings.py
.. * in bacchus/settings.py change the line ALLOWED_HOSTS = [""] to ALLOWED_HOSTS = ["your_hostname"]

10. Create Bacchus admin account
..* [bacchus@localhost]$ python manage.py createsuperuser 

11. Start Bacchus
..* [bacchus@localhost]$ cd scripts
..* [bacchus@localhost]$ ./start_bacchus

12. Access your Bacchus at http://your_hostname:8080/ with the user credentials set in step 10.

Please feel free to contact to openbacchus@gmail.com for any issues.

You can also open issue on GitHub project page.

Hope you enjoy Open Bacchus !

