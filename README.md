# Open Bacchus 
Open Bacchus Project is a backup solution for oVirt/RHEV-M environment. It is being developed based on Python 2.7, Django 1.10 and oVirt Python SDK 4.1. Please be aware that it is still under development.
Thank you for checking it out.

## Preface
Dear Open Bacchus User,

Bacchus is an opensource backup solution for oVirt/RHEV-M. The backup mechanism behind the Bacchus relies on oVirt Python SDK. It basically creates a snapshot of a VM, clones a new VM from the snapshot with the prefix `bacchus_` and exports this cloned VM to default Export Domain of oVirt/RHEV-M. Snapshot and cloned VM is deleted after the backup is completed. Configuration of Export Domain is user's responsibility. If the domain is configured properly, Bacchus will detect it. No additional work required.

The code may be lacking error handling in many cases for now. We are aware of it and will be covering the cases very soon. We need voluntary testers. Please drop an e-mail if you are interested.

We use MariaDB as backend database, you may choose your own flavor but it is your responsibility to take care of it. Celery and RabbitMQ are being used as scheduling backend.


## Installation
### Prerequisites
Please install the following packages on to your favorite Linux distro.
- Python 2.7.x
- pip
- MariaDB
- RabbitMQ

### Installation Steps
1. Install django framework 1.10.x
- *pip install django==1.10.6*
- *pip install django-fernet-fields   (provides encryption in database)*

2. Install oVirt Python SDK
- *pip install ovirt-engine-sdk-python==4.1.2*

3. Install Python MySQL support
- *pip install MySQL-python*

4. Install Celery
- *pip install celery==4.0.2*
- *pip install django-celery-beat*
- *pip install django-celery-results*
- *pip install flower*

5. Create bacchus database and user on MariaDB
- *create database bacchus;*
- *grant all on bacchus.\* to bacchus@localhost identified by 'bacchus';*

6. Create bacchus user on RabbitMQ (run the following commands with root user)
- *rabbitmqctl add_user bacchus bacchus*
- *rabbitmqctl add_vhost bacchus*
- *rabbitmqctl set_user_tags bacchus Administrator*
- *rabbitmqctl set_permissions -p bacchus bacchus ".\*" ".\*" ".\*"*

6. Create bacchus user and group on Linux
- *useradd bacchus*

7. Login with bacchus user and get the Bacchus code from git repository
- *[bacchus@localhost]$ git clone https://github.com/openbacchus/bacchus.git*

8. Create the Bacchus Database layout 
- *cd bacchus*
- *python manage.py check*
- *python manage.py migrate*

9. Add your host into Django settings.py
- in bacchus/settings.py change the line ALLOWED_HOSTS = [""] to ALLOWED_HOSTS = ["your_hostname"]

10. Create Bacchus admin account
- *[bacchus@localhost]$ python manage.py createsuperuser*

11. Start Bacchus
- *[bacchus@localhost]$ cd scripts*
- *[bacchus@localhost]$ ./start_bacchus*

12. Access your Bacchus at http://your_hostname:8080/ with the user credentials set in step 10.

13. We strongly recommend you to configure a reverse proxy with SSL support enabled (e.g. nginx) as a front end to Bacchus.

## How to use Bacchus

As you log in to Bacchus using the default URL, you need to navigate to RHEV-M/Ovirt -> Managers to introduce your oVirt to Bacchus. After successful addition, you may list your VMs under 'VM Protection' pane. You can either use "On Demand Backup" page for spontaneous backups or go to "Automation" pane and define a schedule.

## Restore

Bacchus "restore" functionality has not been implemented yet. VM backups will appear in Export Domain's "Import VM" pane. You may use oVirt/RHEV-M to restore your VM.

## Demo

http://demo.bacchus.co

Please drop an e-mail for demo account.

## Contact Us

Please feel free to contact to openbacchus@gmail.com for any issues.

Subscribe to our user mailing list to stay tuned http://bacchus.co/mailman/listinfo/users_bacchus.co

You can also open an issue on GitHub project page.

Hope you enjoy Open Bacchus !

