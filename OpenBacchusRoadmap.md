# OpenBacchus Roadmap

2019 Roadmap for OpenBacchus app.


- [x] GitHub Organization page
- [ ] Website
- [ ] New Installer
- [ ] Fix the issues on GitHub 
- [ ] New Features
- [ ] Migrate to Patternfly framework 

### Organization Page

Creating the organization page will allow us to oparate on OpenBacchus as a team and more orginazied fasion. First, we need to create personal acconunts in Github, then we transform openbacchus as an organization, and ourselfs as maintainers. This way, we can keep the issues, commits, repos etc. in our new organization and operate on them as a team. For next step, we can create projects and boards to orginize our work and features, create wiki pages and documantations, host our website under our organization etc. Sample organization pages;

- [Google](https://github.com/google)
- [Mongo](https://github.com/topics/mongodb)

More info --> https://blog.github.com/2010-06-29-introducing-organizations/


### Website

Website is a good way to advertise our app. Check out [Atom's](https://atom.io/) (editor) webpage for good starting point. 

### New Installer

Our ansible installer is a good starting point but we need more comments, new installing options and fix some bugs. We might also consider to build an official docker image for instant build. We can create an [Omnibus installer](https://github.com/chef/omnibus) like GitLab's installer. Gitlab, in this section, is the perfect example for us.

### Fix the Issues on GitHub

Our app looks abandoned. Right now it has 10 issues and few feature requests which just needs several hours and little to none attention. We have to start fixing them to attract more users, and give it a new shining look.  

### New Features

We should discuss new features such as;

- [ ] LDAP/AD support
- [ ] Implement oVirt User Interface Plugin to work with bacchus. (feature-request)
- [ ] Retention policy (feature-request) 
- [ ] Proxy support in installer (feature-request)
- [ ] Job-by-Job backups (feature-request)

also we need to check out problems related with the oVirt version 4.2.5 and beyond.

### Migrate to Patternfly Framework

This is a huge step. Migrating the whole app to Patternfly needs lots of time, attention and again, more time. Also, we might need to rewrite all of our work (such as installers, docker images etc.) to support the new framework. Because of this, we should offer the Patternfly framework as an alfa feature and still maintain and develop our legacy Django version. When we complte the previous steps in our Feature List, we can give this one more time while still supporting the legacy version.  
