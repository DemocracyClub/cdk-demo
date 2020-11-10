- `cdk init` needs an empty directory - how to apply to an existing project?

- `cdk init` in general does a lot of stuff I don't want it to do - tried to
 create a virtualenv, makes a README and a sample app. Get out of my way
 ! Might be able to use templates for this, but not easy to see how with a
  ~30 second search

- The python packages are split by AWS service. Good in some ways, but means
 a lot of `pip install aws-cdk.aws-[service]`
 
 - Do we check in the `*.out` directory created after `cdk synth`?
