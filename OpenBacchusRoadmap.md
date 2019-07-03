# OpenBacchus Roadmap

2019 Roadmap for OpenBacchus app.


- [x] GitHub Organization page
- [ ] Website
- [ ] New Installer
- [ ] Fix the issues on GitHub 
- [ ] New Features
- [ ] Migrate to Patternfly framework 

### Organization Page

Creating the organization page will allow us to operate on OpenBacchus as a team and in a more organized fashion. First, we need to create personal accounts in GitHub, then we can transform openbacchus to an organization, and add ourselves as maintainers. This way, we can keep the issues, commits, repos etc. in our new organization and operate on them as a team. For the next step, we can create projects and boards to organize our work and features, create wiki pages and documentation, host our website under our organization etc.

Sample organization pages:

- [Google](https://github.com/google)
- [Mongo](https://github.com/topics/mongodb)

More info --> https://blog.github.com/2010-06-29-introducing-organizations/


### Website

A website is a good way to advertise our app. Check out [Atom's](https://atom.io/) (editor) webpage for good starting point. 

### New Installer

Our ansible installer is a good starting point but we need more comments, new installation options and some bug fixes. We might also consider building an official docker image for instant deployment. We can create an Omnibus installer like GitLab's installer. Gitlab is a perfect example for us.

### Fix the Issues on GitHub

Our app looks abandoned. Right now, it has 10 issues and few feature requests which just need a few hours and a little effort. We have to start fixing them to attract more users, and give it a shiny new look.

### New Features

We should discuss new features such as;

- [ ] LDAP/AD support
- [ ] Implement oVirt User Interface Plugin to work with bacchus. (feature-request)
- [ ] Retention policy (feature-request) 
- [ ] Proxy support in installer (feature-request)
- [ ] Job-by-Job backups (feature-request)

Also we need to analyse the problems related to oVirt version 4.2.5 and later.

### Migrate to Patternfly Framework

This is a huge step. Migrating the whole app to Patternfly needs lots of time, effort and again, more time. Also, we might need to redo installers, docker images etc. to support the Patternfly framework. Because of this, we should offer the Patternfly framework as an alpha feature and still maintain and develop the legacy Django version. When we complete the previous steps in our Feature List, we can give this one more time while still supporting the legacy version.  
