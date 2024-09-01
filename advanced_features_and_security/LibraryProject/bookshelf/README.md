Permissions and Groups Setup
==========================

In this application, we use Django's built-in permission system to control access to various parts of the application.

We have three groups: Editors, Viewers, and Admins. Each group has assigned permissions as follows:

* Editors: can_edit, can_create
* Viewers: can_view
* Admins: can_view, can_create, can_edit, can_delete

We use decorators such as `permission_required` to enforce these permissions in our views.

To test the implementation, create test users and assign them to different groups. Then, log in as these users and attempt to access various parts of the application to ensure that permissions are applied correctly.