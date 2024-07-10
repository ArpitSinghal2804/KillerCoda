![Dan](../../assets/yellow-belt-devops-dojo/test-driven-development/dan.png) 

> I now need to add the code to make the unit tests pass.

# Steps

* Head over to the branch of the pull request which you named `us-4-searchbyfirstname` in the previous step, to edit the file where search by last name is happening: [`/src/main/java/org/springframework/samples/petclinic/owner/OwnerRepository.java`](https://[[HOST_SUBDOMAIN]]-9876-[[KATACODA_HOST]].environments.katacoda.com/#ownerrepository)
* Click on the pencil icon in the top right corner to edit the file
* Paste below code after line 46: 
<pre class="file" data-target="clipboard">

    /**
     * Retrieve {@link Owner}s from the data store by first name, returning all owners
     * whose first name <i>starts</i> with the given name.
     * @param firstName Value to search for
     * @return a Collection of matching {@link Owner}s (or an empty Collection if none
     * found)
     */
    @Query("SELECT DISTINCT owner FROM Owner owner left join fetch owner.pets WHERE owner.firstName LIKE :firstName%")
    @Transactional(readOnly = true)
    Collection&lt;Owner&gt; findByFirstName(@Param("firstName") String firstName);
</pre>

* Choose commit in the same branch (`us-4-searchbyfirstname`), so that edits happen in the context of the existing pull request
* Navigate to <a href="https://[[HOST_SUBDOMAIN]]-8080-[[KATACODA_HOST]].environments.katacoda.com/blue/organizations/jenkins/pet-clinic/pr" target="jenkins">Jenkins</a> and verify that the build stage works, even if functionality is still not 100% developed
* When the deploy stage in Jenkins is done, navigate to the [Pet Clinic application](https://[[HOST_SUBDOMAIN]]-9966-[[KATACODA_HOST]].environments.katacoda.com/), click "Find Owners", and search for `Betty`{{copy}}. The application will not return any result: the feature is not fully implemented yet.

💡 TIP: If you click "Find owners" in the Pet Clinic, without entering any name, you will get all the pet owners.
