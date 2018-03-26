# Open Bacchus 
Open Bacchus Project is a backup solution for oVirt/RHV environment. It is being developed based on Python 2.7, Django 1.10 and oVirt Python SDK 4.1. Please be aware that it is still under development.
Thank you for checking it out.

## Preface
Dear Open Bacchus User,

Bacchus is an opensource backup solution for oVirt/RHV. The backup mechanism behind the Bacchus relies on oVirt Python SDK. It basically creates a snapshot of a VM, clones a new VM from the snapshot with the prefix `bacchus_` and exports this cloned VM to default Export Domain of oVirt/RHV. Snapshot and cloned VM is deleted after the backup is completed. Configuration of Export Domain is user's responsibility. If the domain is configured properly, Bacchus will detect it. No additional work required.

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

4. Point your browser to `https://<bacchus_hostname>/` which you set in your settings.yml file. NGINX is a part of Bacchus now and it is installed with a self-signed certificate by default.


### Updates

Please re-run the installer `# ansible-playbook installer.yml`, it will fetch the latest codes and update your current environment.


### Notifications

Please use the "Settings" section in Bacchus Web Console to get notified by e-mail.


### Stop/Start Bacchus

The installer will place the systemd scripts in to your OS after a successful installation. You can use the `systemctl <stop/start/status> bacchus` command to stop/start the Bacchus services.

Under `<bacchus_base_path>/logs` directory, you will find the log files.

## How to use Bacchus

As you log in to Bacchus using the default URL, you need to navigate to RHV/Ovirt -> Managers to add your Virtualization Manager to Bacchus. After successful addition, you may list your VMs under 'VM Protection' pane. You can either use "On Demand Backup" page for instant backups or go to "Automation" pane and define a schedule. 

By default, Bacchus will run a discovery job every 10 minutes to detect the changes in your environment. You can change this interval in settings.yml file by changing the `inv_sched_interval` parameter. This job has a minimal impact on your system, so you do not need to worry about it.


## Restore

Bacchus "restore" functionality has not been implemented yet. VM backups will appear in Export Domain's "Import VM" pane. You may use oVirt/RHV to restore your VM.

## DEMO

Please find the demo site at https://openbacchus.com

username : demo

password : bacchusdemo


## Contact Us

Please feel free to contact to openbacchus@gmail.com for any issues.

Follow us on twitter @openbacchus

You can also open an issue on GitHub project page.

Hope you enjoy Open Bacchus !

## Donate

Please donate ! https://www.patreon.com/openbacchus

We need more resources for a better development and testing environment.

Thank you !

## Credits
Special thanks to JetBrains for supporting Open Bacchus.

![JetBrains](https://github.com/openbacchus/bacchus/blob/master/jetbrains.png)
