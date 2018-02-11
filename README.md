# Open Bacchus 
Open Bacchus Project is a backup solution for oVirt/RHEV environment. It is being developed based on Python 2.7, Django 1.10 and oVirt Python SDK 4.1. Please be aware that it is still under development.
Thank you for checking it out.

## Preface
Dear Open Bacchus User,

Bacchus is an opensource backup solution for oVirt/RHEV. The backup mechanism behind the Bacchus relies on oVirt Python SDK. It basically creates a snapshot of a VM, clones a new VM from the snapshot with the prefix `bacchus_` and exports this cloned VM to default Export Domain of oVirt/RHEV. Snapshot and cloned VM is deleted after the backup is completed. Configuration of Export Domain is user's responsibility. If the domain is configured properly, Bacchus will detect it. No additional work required.

The code may be lacking error handling in many cases for now. We are aware of it and will be covering the cases very soon. We need voluntary testers. Please drop an e-mail if you are interested.

We use MariaDB as backend database, you may choose your own flavor but it is your responsibility to take care of it. Celery and RabbitMQ are being used as scheduling backend.


## Installation
### Prerequisites
You need to have the following packages installed in your CentOS or RHEL
- ansible > 2.0
- wget


### Installation Steps
1.  Retrieve the ansible playbook from GitHub repository.

`# wget https://raw.githubusercontent.com/openbacchus/bacchus/master/installer.yml`

`# wget https://raw.githubusercontent.com/openbacchus/bacchus/master/settings.yml`

2. Change the default settings in the settings.yml file.

3. Run the playbook with root privilege:

`# ansible-playbook installer.yml`

## How to use Bacchus

As you log in to Bacchus using the default URL, you need to navigate to RHEV/Ovirt -> Managers to introduce your oVirt to Bacchus. After successful addition, you may list your VMs under 'VM Protection' pane. You can either use "On Demand Backup" page for spontaneous backups or go to "Automation" pane and define a schedule.


## Restore

Bacchus "restore" functionality has not been implemented yet. VM backups will appear in Export Domain's "Import VM" pane. You may use oVirt/RHEV to restore your VM.


## Contact Us

Please feel free to contact to openbacchus@gmail.com for any issues.

Subscribe to our user mailing list to stay tuned http://bacchus.co/mailman/listinfo/users_bacchus.co

You can also open an issue on GitHub project page.

Hope you enjoy Open Bacchus !

