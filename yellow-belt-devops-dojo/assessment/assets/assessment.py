#!/usr/bin/python3

# import system from os
from os import system

module_welcome = "welcome"
module_leading_change = "Leading Change"
module_version_control = "Version Control"
module_continuous_integration = "Continuous Integration"
module_value_stream_mapping = "Value Stream Mapping"
module_devops_kaizen = "DevOps Kaizen"
module_continuous_testing = "Continuous Testing"
module_test_driven_development = "Test Driven Development"
module_shift_left_on_security = "Shift Left On Security"
module_post_incident_practices = "Post Incident Practices"

class Question:
     def __init__(self, prompt, answer, module):
          self.prompt = prompt
          self.answer = answer
          self.module = module

# Question bank
question_prompts = [
     "Q1. Who was appointed as the DevOps coach for the Pet Clinic DevOps transformation?\n\n\n(a) Charlie\n\n(b) Paulo\n\n(c) Chun\n\n(d) Hal\n\n",
     "Q2. Blameless post-mortems are conducted to determine?\n\n\n(a) What caused a problem?\n\n(b) Who caused the problem?\n\n(c) Where a problem happened?\n\n",
     "Q3. Which of the following are key to successful DevOps Transformations?\n\n\n(a) Continuous Improvement via DevOps Kaizen Events\n\n(b) Value Stream Mapping \n\n(c) Prioritizing culture over tooling\n\n(d) All of the above\n\n",
     "Q4. What is the recommended first step in a DevOps Transformation?\n\n\n(a) DevOps Kaizen\n\n(b) Value Stream Mapping\n\n(c) Improvement Themes\n\n",
     "Q5. Which of the following is the defacto standard for version control systems?\n\n\n(a) Git\n\n(b) Subversion\n\n(c) Jira\n\n",
     "Q6. Select the attributes of a successful branching model?\n\n\n(a) Short lived feature branches\n\n(b) Changes committed often\n\n(c) Master branch never contains broken code\n\n(d) All of the above\n\n",
     "Q7. What type of request is submitted in order to receive feedback on the work performed in a feature branch?\n\n\n(a) Pull Request \n\n(b) Push Request \n\n(c) Commit Request\n\n",
     "Q8. Which of these is an open source automation server?\n\n\n(a) GitHub\n\n(b) Jira\n\n(c) Jenkins\n\n",
     "Q9. An applications continuous integration pipeline is stored in which file?\n\n\n(a) DockerFile\n\n(b) Jenkinsfile\n\n(c) CODEOWNERS\n\n",
     "Q10. Which of the following actions can a Jenkins pipeline perform?\n\n\n(a) Compile Code\n\n(b) Run Automated Tests\n\n(c) Lint files\n\n(d) All of the above\n\n",
     "Q11. How long does it take for a feature to be delivered?\n\n\n(a) The time work spends waiting\n\n(b) The actual time someone works on it\n\n(c) The time work spends waiting + the actual time someone works on it\n\n",
     "Q12. Select the reasons work spends time waiting?\n\n\n(a) Handoffs\n\n(b) Queues\n\n(c) Incomplete / Incorrect Processing\n\n(d) All of the above\n\n",
     "Q13. Which metrics are captured for each process step in a value stream map?\n\n\n(a) Lead time\n\n(b) Processing Time\n\n(c) % Complete & Accurate\n\n(d) All of the above\n\n",
     "Q14. What step typically follows a Value Stream Mapping workshop?\n\n\n(a) DevOps Kaizen Event\n\n(b) Scrum\n\n(c) PI Planning\n\n",
     "Q15. How long is recommended for a Kaizen increment?\n\n\n(a) 2 weeks\n\n(b) 6 months\n\n(c) 1 quarter\n\n",
     "Q16. Which of the following is not a section in an Improvement Theme?\n\n\n(a) Definition of Awesome\n\n(b) Definition of Done\n\n(c) Next Target Condition\n\n",
     "Q17. Where should we run our unit and functional tests?\n\n\n(a) In production\n\n(b) In our Continuous Delivery/Deployment Pipeline\n\n(c) In our Continuous Integration Pipeline\n\n",
     "Q18. In the context of the test pyramid which type of tests are considered to be the most stable?\n\n\n(a) Manual Tests\n\n(b) Automated GUI Tests\n\n(c) Automated Unit Tests\n\n",
     "Q19. To achieve continuous testing when should you be running your unit tests?\n\n\n(a) On every code commit\n\n(b) On every deployment\n\n(c) Manually as needed\n\n",
     "Q20. Identify the steps in Test Driven Development?\n\n\n(a) Write code to pass test, Write unit test which fails, Verify test passes, Refactor code and repeat as needed\n\n(b) Write unit test that fails, Write code to pass test, Verify test passes, Refactor code and repeat as needed\n\n(c) Write code to pass test, Write unit test that fails, Refactor code and repeat as needed, Verify test passes\n\n",
     "Q21. Who is responsible for verifying an application has sufficient unit test coverage?\n\n\n(a) Product Owner\n\n(b) Scrum Master\n\n(c) Developers\n\n(d) The entire team\n\n",
     "Q22. When should we run our unit tests?\n\n\n(a) On every code commit\n\n(b) When a pull request is merged\n\n(c) On every code commit and when every pull request is merged\n\n",
     "Q23. Which type of security testing should be included in a CI Pipeline?\n\n\n(a) Static Application Security Testing (SAST)\n\n(b) Dynamic Application Security Testing (DAST)\n\n",
     "Q24. Why do we shift security left?\n\n\n(a) To move it towards the original cause of the vulnerabilities\n\n(b) To keep it away from the original cause of the vulnerabilities\n\n",
     "Q25. What is a dependency checker used for?\n\n\n(a) To perform static application security testing\n\n(b) Detect publicly disclosed vulnerabilities within a project's dependencies \n\n(c) To perform dynamic application security testing\n\n",
     "Q26. Which is the recommended approach for post incident practices?\n\n\n(a) Value Stream Mapping workshop\n\n(b) DevOps Kaizen event\n\n(c) Blameless post-mortem\n\n(d) Surface level post incident reviews\n\n",
     "Q27. Which of the following behaviors are likely to occur in a blameful culture?\n\n\n(a) People giving full and frank accounts of their actions which may have contributed to the outage\n\n(b) Team feeling empowered to act and being recognized for doing so\n\n(c) Leaders being more informed in relation to what is actually happening\n\n(d) None of the above\n\n",
     "Q28. Which is the key metric to focus on in Post Incident Practices?\n\n\n(a) Mean time to recover (MTTR)\n\n(b) Mean time to isolate (MTTI)\n\n(c) Mean time to fix (MTTF)\n\n"
]

questions = [
     Question(question_prompts[0], "c", module_welcome),
     Question(question_prompts[1], "a", module_leading_change),
     Question(question_prompts[2], "d", module_leading_change),
     Question(question_prompts[3], "b", module_leading_change),
     Question(question_prompts[4], "a", module_version_control),
     Question(question_prompts[5], "d", module_version_control),
     Question(question_prompts[6], "a", module_version_control),
     Question(question_prompts[7], "c", module_continuous_integration),
     Question(question_prompts[8], "b", module_continuous_integration),
     Question(question_prompts[9], "d", module_continuous_integration),
     Question(question_prompts[10], "c", module_value_stream_mapping),
     Question(question_prompts[11], "d", module_value_stream_mapping),
     Question(question_prompts[12], "d", module_value_stream_mapping),
     Question(question_prompts[13], "a", module_devops_kaizen),
     Question(question_prompts[14], "a", module_devops_kaizen),
     Question(question_prompts[15], "b", module_devops_kaizen),
     Question(question_prompts[16], "c", module_continuous_testing),
     Question(question_prompts[17], "c", module_continuous_testing),
     Question(question_prompts[18], "a", module_continuous_testing),
     Question(question_prompts[19], "b", module_test_driven_development),
     Question(question_prompts[20], "d", module_test_driven_development),
     Question(question_prompts[21], "c", module_test_driven_development),
     Question(question_prompts[22], "a", module_shift_left_on_security),
     Question(question_prompts[23], "a", module_shift_left_on_security),
     Question(question_prompts[24], "b", module_shift_left_on_security),
     Question(question_prompts[25], "c", module_post_incident_practices),
     Question(question_prompts[26], "d", module_post_incident_practices),
     Question(question_prompts[27], "a", module_post_incident_practices)
]

def run_quiz(questions):

     # Get first name of the user
     firstname = ""
     try:
          myfile = open('/tmp/firstname.txt', 'r')
          firstname = myfile.read().replace('\n', '')
     except IOError:
          firstname = "student"

     score = 0
     score_version_control = 0
     score_leading_change = 0
     score_continuous_integration = 0
     score_value_stream_mapping = 0
     score_devops_kaizen = 0
     score_continuous_testing = 0
     score_test_driven_development = 0
     score_shift_left_on_security = 0
     score_post_incident_practices = 0

     # welcome the student
     system("clear")
     print("\033[1;32;40m Welcome " + firstname + " shall we play a game?\n")
     print("\033[1;32;40m You have nearly completed your DevOps Yellow Belt.\n")
     print("\033[1;32;40m Complete this assessment and you are there.\n\n")
     print("\033[1;34;40m Instructions:\n\n")
     print("\033[1;34;40m Click anywhere on this terminal window to activate the cursor.\n")
     print("\033[1;34;40m Press return to start the assessment.\n")
     print("\033[1;34;40m When you have answered a question press return to proceed to the next question.\n\n")
     input("\033[1;33;40m This is the way!")

     system("clear")

     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
               # update the module scores
               if module_continuous_integration == question.module:
                    score_continuous_integration +=1
               elif module_version_control == question.module:
                    score_version_control +=1
               elif module_leading_change == question.module:
                    score_leading_change +=1
               elif module_continuous_integration == question.module:
                    score_continuous_integration +=1
               elif module_value_stream_mapping == question.module:
                    score_value_stream_mapping +=1
               elif module_devops_kaizen == question.module:
                    score_devops_kaizen +=1
               elif module_continuous_testing == question.module:
                    score_continuous_testing +=1
               elif module_test_driven_development == question.module:
                    score_test_driven_development +=1
               elif module_shift_left_on_security == question.module:
                    score_shift_left_on_security +=1
               elif module_post_incident_practices == question.module:
                    score_post_incident_practices +=1
          system("clear")

     # candidate has to
     # answer 18 out of 27 questions
     # get at least 18 questions right from each module
     if score > 18 and score_continuous_integration >= 2 and score_version_control >=2 \
          and score_leading_change >=2 and score_value_stream_mapping >=2 and score_devops_kaizen >=2 \
          and score_continuous_testing >=2 and score_test_driven_development >=2 \
          and score_shift_left_on_security >=2 and score_post_incident_practices >=2 :
          print("\033[1;32;40m You got", score, "out of", len(questions), "\n")
          print("\033[1;32;40m Congratulations " + firstname + " you have passed the assessment and have earned your DevOps Yellow Belt.\n")
          print("\033[1;32;40m Use the dojo - This is the way!\n")
          open('/tmp/assessment.txt', 'w')
     else:
          print("\033[1;31;40m You got", score, "out of", len(questions), "\n")
          print("\033[1;31;40m Unfortunately " + firstname + " you haven't passed the assessment.\n")
          print("\033[1;32;40m You have a bit more work to do to get your DevOps Yellow Belt.\n")
          print("\033[1;32;40m Rest assured the answers are out there.\n\n Please review the following hints as to where the answers may be.\n")
          if score_continuous_integration < 2:
               print("\033[1;33;40m Take another look at the Continuous Integration module before retaking the assessment.\n")
          if score_version_control < 2:
               print("\033[1;33;40m You may want to review the Version Control module before resitting the assessment.\n")
          if score_leading_change < 2:
               print("\033[1;33;40m Spend some more time on the Leading Change module before taking the assessment.\n")
          if score_value_stream_mapping < 2:
               print("\033[1;33;40m Review the Value Stream Mapping module before retaking the assessment.\n")
          if score_devops_kaizen < 2:
               print("\033[1;33;40m Retake the DevOps Kaizen module before resitting the assessment.\n")
          if score_continuous_testing < 2:
               print("\033[1;33;40m Revisit the Continuous Testing module before taking the assessment.\n")
          if score_test_driven_development < 2:
               print("\033[1;33;40m Go back and retake the Test Driven Development module before trying assessment again.\n")
          if score_shift_left_on_security < 2:
               print("\033[1;33;40m Make another run at the Shift Left On Security module before attempting the assessment again.\n")
          if score_post_incident_practices < 2:
               print("\033[1;33;40m Spend some more cycles on the Post Incident Practices module before resitting the assessment.\n\n")
          print("\033[1;32;40m Use the dojo - This is the way!\n")
run_quiz(questions)
