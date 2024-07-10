![Dan](../../assets/yellow-belt-devops-dojo/test-driven-development/dan.png)

> Final step is to update the label of the web form, and we will be good to go.

# Steps

* Continuing in the branch of the pull request named `us-4-searchbyfirstname`, let's edit the view: [`/src/main/resources/templates/owners/findOwners.html`](https://[[HOST_SUBDOMAIN]]-9876-[[KATACODA_HOST]].environments.katacoda.com/#findowners)
* Click on the pencil icon in the top right corner to edit the file.
* Replace Line 12 by the below code:

`<label class="col-sm-2 control-label">Last/First name </label>`{{copy}}

* Choose commit in the same branch (`us-4-searchbyfirstname`), so that edits continue to happen in the context of the same pull request.
* Navigate to <a href="https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/blue/organizations/jenkins/pet-clinic/pr" target="jenkins">Jenkins</a> and verify that the build stage works.
* Navigate to the [Pet Clinic application](https://[[HOST_SUBDOMAIN]]-9966-[[KATACODA_HOST]].environments.katacoda.com/), click "Find Owners", and search for `Betty`{{copy}}. Check that the label is "Last/First name", and that the application properly finds the owners by first name.
