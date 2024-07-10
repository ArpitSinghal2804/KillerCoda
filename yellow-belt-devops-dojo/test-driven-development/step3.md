![Dan](../../assets/yellow-belt-devops-dojo/test-driven-development/dan.png) ![Tina](../../assets/yellow-belt-devops-dojo/test-driven-development/tina.png) 

**Previously**, **Dan** would developer test an implemented feature locally. Then once he was happy with the feature he would include it in the working build, which would be prepared nightly for QA/Testing. **Tina** would then manually test the implemented feature against pre-written test cases. If the tests passed and the implemented feature met the acceptance criteria for the story and it was considered to be potentially shippable code and would be included in the build for the sprint demo. Paulo would then be expected to confirm the story meets the definition of done during the sprint demo.

Dan's and Tina's teams as part of the companies DevOps journey and in support of the 2nd DevOps way "Amplify Feedback Loops", have adopted a TDD approach as part of their process improvements to shorten and amplify feedback loops. This is to allow necessary corrections to be identified and remediated as close to source as possible.

**Now**, Dan and Tina review each user story and translate requirements into tests, they write the unit tests first, Dan then writes enough code to make the tests fail. Code is built and the automated tests are then run to verify the tests fail. Then Dan fixes the code to make the test pass, another code change is committed, the code is built, and the automated tests run to verify that the tests pass.

In short, the flow looks like this:
* Write unit tests to cover the user story
* Check that the tests fail
* Write enough code to pass the test
* Verify that the test passes
* Refactor the code
* Repeat

This is **Test Driven Development**. 
