#!/usr/bin/env groovy

currentBuild.description = ""

pipeline {

  agent any

  stages {

    stage('Review content') {

      // The following review elements review the raw content, and do not require the site to be built first
      parallel {

        stage('Spell Check') {
          agent {
            dockerfile {
              filename 'Dockerfile.mdspell'
              args '-u="root" -v $WORKSPACE:/srv/jekyll -w /srv/jekyll --entrypoint=""'
              reuseNode true
            }
          }
          environment {
            // mdspell uses chalk to color output.
            // chalk uses a library called supports-color which auto-detects terminal support.
            // this env var will force the library to use color.
            FORCE_COLOR = "1";
          }
          steps {
             echo 'Checking spelling...'
             sh  '''
             mdspell -V
             find . -type f \\( -iname "*.md" ! -iname "*nospell*" \\) | xargs mdspell -n -a -r --en-us --dictionary dicts/en_US-large
             '''
          }
        }
        stage('Python linting') {
          when { changeset "yellow-belt-devops-dojo*/*/assets/*.py" }
          agent {
              docker { //TRACK_DOCKER_TAGS[dockerhub|cytopia/pylint:latest]
                  image 'cytopia/pylint:latest'
                  args "-u root --entrypoint=''"
                  reuseNode true
              }
          }
          steps {
            sh "pylint --version || true; pylint --disable=all --enable=F,E,unreachable,duplicate-key,unnecessary-semicolon,global-variable-not-assigned,unused-variable,binary-op-exception,bad-format-string,anomalous-backslash-in-string,bad-open-mode --disable=unused-variable,import-error --msg-template='{path}:{line}:{column}: {msg_id}: {msg} ({symbol})' yellow-belt-devops-dojo*/*/assets/*.py"
          }
        }
        stage('Yaml linting') {
          when { changeset "yellow-belt-devops-dojo*/*/assets/*.yaml" }
          agent {
              docker { //TRACK_DOCKER_TAGS[dockerhub|cytopia/yamllint:1.23]
                  image 'cytopia/yamllint:1.23'
                  args "-u root --entrypoint=''"
                  reuseNode true
              }
          }
          steps {
            sh "yamllint --version || true; yamllint -c config/yamllint_config yellow-belt-devops-dojo*/*/assets/*.yaml"          }
        }
        stage('JSON linting') {  // Find all files with errors and not just the first.
          when { changeset "**/*.json" }
          agent {
              docker { //TRACK_DOCKER_TAGS[dockerhub|sahsu/docker-jsonlint] cytopia version has no -q flag
                  image 'sahsu/docker-jsonlint'
                  args "-u root --entrypoint=''"
                  reuseNode true
              }
          }
          steps {  // jsonlint doesn't support glob expansion yet https://github.com/zaach/jsonlint/pull/104
            sh 'jsonlint --version || exit 0'
            script {
              errCount = 0
              sFiles = findFiles(glob: '**/*.json')
              sFiles.each { filename ->
                  try {
                      sh "jsonlint -q ${filename}"
                  }
                  catch (err) {
                      println "Error on ${filename}"
                      errCount++
                  }
              }
              if (errCount) {
                msg = errCount + " JSON file(s) in error."
                println msg
                currentBuild.description = currentBuild.description + msg
                currentBuild.result = 'FAILURE'
              }
            }
          }
        }
      }
    }
  }
}
