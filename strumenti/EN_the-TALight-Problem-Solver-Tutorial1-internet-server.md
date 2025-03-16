#### User Guide Area - Problem Solver TUTORIAL 1:
# HOW TO ACCESS FROM A CLI A TALIGHT SERVER IN THE INTERNET

This first tutorial on how to use TALight assumes that you can launch the `rtal` client from a `bash` like Command Line Interpreter (CLI). Here are two ways in which you can meet this requirement:

1. if you have at least a partial installation of TALight on your machine. See Section [TALight Installation](https://github.com/romeorizzi/TALight/wiki/EN_TALight-Installation) for instructions on how to get such an installation.
2. if for any reason you do not want or cannot install anything on your machine then the [TALight from the Browser](https://github.com/romeorizzi/TALight/wiki/EN_TALight-from-the-Browser) Section of this Wiki shows how you can get access from your browser to a functioning `bash` CLI environment where the `rtal` client is installed.


Either way you can now make use of TALight problems and access their services as a problem solver, as long as they are deployed in the internet and made available to you.


## Some commands to prove the available functionalities

**We assume that, in one way or the other ([TALight on browser](https://github.com/romeorizzi/TALight/wiki/EN_TALight-Browser-replit) or [TALight Installation](https://github.com/romeorizzi/TALight/wiki/EN_TALight-Installation)), you now have the terminal and an `rtal` executable properly placed and working as explained above.**

Free exploration is the intended approach within TALight, but, just to give you a first start with this, here are a few examples of commands one could issue to explore what services are offered by the tutorial problems collection hosted at `wss://ta.di.univr.it/esame`.


From here, try out the following actions.

To get general help on the `rtal` command and its subcommands:

```bash 
rtal -s wss://ta.di.univr.it/esame help
```

From the visualized help page you might learn that the option `--server`, or just `-s` in short, allows you to specify the URL of the server to which the `rtal` client is sending the request. Therefore, your request has travelled through the internet and the help page has been served to you from `wss://ta.di.univr.it/esame`. 

To get more specific help on an `rtal` subcommand:

```bash 
rtal -s wss://ta.di.univr.it/esame list
```

Therefore, to see the whole list of problems currently available on our tutorial collection as deployed from `wss://ta.di.univr.it/esame`, use the `list` subcommand of the `rtal command` without imposing any filter:

```bash 
rtal -s wss://ta.di.univr.it/esame list
```

Different problem collections may comprise and offer completely different sets of problems.
Therefore, the returned list of the available problems will depend on the URL you have specified after the `-s` option. This option is explaind when you run `rtal --help`. If you entirely omit this option then the `rtal` client will try to send your request to an `rtald` daemon running in local. If no such daemon is running on your local machine then you get

```bash
 ERROR rtal > Cannot connect to ws://127.0.0.1:8080/
```

We assume you launched the whole command above, or you entirely omitted the `-s` option but launched the command after properly launching the `rtald` daemon in local using the `-d` option to ask it to serve the problems of the tutorial (as explained in Section [The Problem Solver Tutorial 2 - local server access from the CLI](https://github.com/romeorizzi/TALight/wiki/EN_the-TALight-Problem-Solver-Tutorial2-local-server).  

In this case, the returned list of the available problems should contain, among many others, the example problem `sum` that we are going to explore next.
With:

```bash 
rtal -s wss://ta.di.univr.it/esame get sum
```

you invoke the `get` subcommand to download the `.tar` file `sum.tar`. This file is the archive of the public folder of problem `sum` on the `wss://ta.di.univr.it` server. Once you untar this folder, you find into it the statement of the problem `sum` and all other material relating to the problem (explanations, videos, links, ...) that the problem maker has collected and decided to make public (i.e., accessible to you through this simple mechanism). The folder `public` may be a rich tree of directories, and the whole tree, together with any material that is symlinked from within the tree (even if the material il placed outside) will then end up in the archive downoladed by the problem solver.

<details><summary><b>How to untar an archive</b></summary>  

Untar with:

```bash
tar -xvf sum.tar
```

If the archive is zipped (you can understand this since the extension will be either `.tgz` or `.tar.zip` insetad than `.tar`):


```bash 
tar -xvzf sum.tgz
```

On Windows you can also use any utility like 7-Zip or WinZip.

</details>

The list subcommand also offers a rudimentary search facility.
If you issue

```bash 
rtal -s wss://ta.di.univr.it/esame list sum
```

or 

```bash 
rtal -s wss://ta.di.univr.it/esame list um
```

you will be returned a list comprising only of the problem `sum` since it is currently the only problem whose name contains the `um` substring.
This filtering capability actually supports any regular expression.
For example, with

```bash 
rtal -s wss://ta.di.univr.it/esame list ^p[a-z]*$
```

you get the list of all those problems in the collection whose name contains only lower-case letters and begins with `p`. In regular expressions the `^` and `$` characters are used to impose a match from the very beginning and up to the very end of the candidate string.


## Exploring the services available for a problem

By using the `-v` flag of the `list` subcommand like in

```bash 
rtal -s wss://ta.di.univr.it/esame list -v
```

or in

```bash 
rtal -s wss://ta.di.univr.it/esame list -v ^p[a-z]*$
```

you get a more verbose output where, for each problem in the collection (whose name contains only lower-case letters and begins with `p`, as for in the second case), all services currently available for that problem are also listed out in a sublist.
Usually you are interested in exploring the services for the sole problem on which you are working. The best way to conduct this sort of exploration is by means of the `synopsis` service that will be presented more below. However, just for now, also the filtering mechanism can be used:

Entering:

```bash 
rtal -s wss://ta.di.univr.it/esame list sum
```

or, more specifically:

```bash 
rtal -s wss://ta.di.univr.it/esame list ^sum$
```
you will get the following output:

```
- sum
  * free_sum
    # lang [it]
    # num_questions [10]
    # numbers [twodigits]
    # obj [any]
  * help
    # lang [it]
    # page [help]
  * sum_and_difference
    # lang [it]
    # num_questions [10]
    # numbers [onedigit]
  * sum_and_product
    # lang [it]
    # num_questions [10]
    # numbers [onedigit]
  * synopsis
    # lang [it]
    # service [synopsis]
```

In this way you learn that 5 services are currently available for problem `sum`:
`free_sum`, `sum_and_difference`, `sum_and_product`, `help` and `synopsis`.
For each of these services you also get the sublist of its arguments. An argument may have a default value (reported within the brackets), in which case the argument is optional. Otherwise the argument is mandatory. When an argument is optional and you do not specify a value for it, then its default value is assumed.

But how do you know the set of possible values for a given parameter?
To verbose out all possible options for the arguments use:

```bash 
rtal -s wss://ta.di.univr.it/esame list sum -v
```

Here you should get a list with the very same length and items as the one displayed above, but the description of the items is now expanded.
For example, looking only at the items relating to the `free_sum` service we now read:

```bash 
  * free_sum
    # lang [it] ^(hardcoded|en|it)$
    # num_questions [10] ^([1-9]|[1-2][0-9]|30)$
    # numbers [twodigits] ^(onedigit|twodigits|big)$
    # obj [any] ^(any|max_product)$
```
Notice how the possible values of an argument are specifyied by means of a regular expression.
Therefore, the 3 possible values for the argument `lang` are `hardcoded`, `en` and `it` whereas the 30 possible values for the argument `num_questions` are the integers in the closed interval [1,30].
We refer to [regexp syntax](https://docs.rs/regex/1.4.3/regex/#syntax) to know more about the syntax of the regular expressions we have adopted (the standard ones for the Rust language).

From these output you might infer that the three services `sum`, `sum_and_difference`, and `sum_and_product` are meant to conduct a dialogue where you (or a bot you designed to act on your behalf) will be asked 10 questions (all instances of a problem defined by the service). Indeed, 10 is the default value for the parameter `num_questions`. You can specify a different value for this parameter which can take only integers in the interval $[1,30]$ as specified by the regexp `^([1-9]|[1-2][0-9]|30)$` reported above.

Combining the problem specific information you got by issuing `rtal list sum -v` with the TALight core instructions got with `rtal connect --help` you could decide to try out the service `free_sum`:

```bash
rtal -s wss://ta.di.univr.it/esame  connect sum free_sum
```

And also try to call it with other non-standard combinations for its arguments: 

```bash
rtal -s wss://ta.di.univr.it/esame  connect -a num_questions=13 -a numbers=onedigit sum sum_and_product
```

Connecting to the services in this direct way you will enjoy a direct interaction with the server through the terminal. This can help you to find out about the service and the protocol of the interaction.
Actively experiment also with the arguments of the service, they are thought to help you and sometimes they are also meant to offer an excalation on a problem that starts simple to better approach your curiosity and open mindness. Try for example:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -a numbers=big sum free_sum
```

or

```bash
rtal -s wss://ta.di.univr.it/esame  connect -a obj=max_product sum free_sum
```

### the `synopsis` service 

All problems offer a `synopsis` service. This is meant to provide help and convey time contextual information on the porpuse, usage, and syntax for a best possible use of any service problem. To specify the service use the `service` argument as follows:

```bash
./rtal -s wss://ta.di.univr.it/esame connect sum synopsis -a service=free_sum
```

In this syntax `synopsis` is regarded as a service of the problem `sum` and has ben called with its `service` argument set to `free_sum`.
In this way the user gets all the pertinent information on the `free_sum` service of the `sum` problem. In particular, the user gets a list of all the arguments of the `free_sum` service. The `synopsis` service is much more informative and supportive than the `list` subcommand since it also provides meaning, intended use, and examples.

To know more about the `synopsis` service just call it as follows.

```bash
./rtal -s wss://ta.di.univr.it/esame connect sum synopsis
```

Indeed, the default argument for the synopsis service is usually `synopsis` itself.


### the `help` service 

Problem `sum` also offers an `help` service

```bash
./rtal -s wss://ta.di.univr.it/esame connect sum -a page=sum_and_difference help
```

This is meant to expose a sort of man pages on a problem. What written in these pages is less constrained and follows a less rigid format than the information conveyed by the `synopsis` service.
However, currently we have done this only for the `sum` problem and we still have to take decisions on whether and how to structure and/or organize this further information channel.


## Interactive Services

Some services will interact with the problem solver only in order to get in all the input data they need. Other services demand higher levels of interaction. The protocol of the interaction has been designed in full freedom by the problem maker. Its details or general idea may have been described in the statement of the problem, or may get revealed through the synopsis service or get dispelled by experimenting with the service and its arguments. We have already seen above a few examples of interaction based services, like the service `free_sum` of the problem `sum` which you can invoke by issuing:  

```bash 
rtal -s wss://ta.di.univr.it/esame connect sum free_sum
```

It is quite natural for humans to grasp the simple structure of this interaction and its underling protocol.

## Interactive services and bots

After you have got what competence the problem is trying to address, and the protocol for your interaction with it, you can then go for making a bot exhibiting that competence on your behalf.

The plug in of the bot follows this simple template/mechanism:

```bash
rtal <problem_collection> connect <problem> <service> -- <my_executable_bot>
```

where the bot containing your solution is assumed to ultimately be an executable command on your machine. It is also assumed that your bot exchanges with the outside world through the stdin and stdout (and stderr if you want to debug it) streams.
(The standard but not required assumption is that it is also located on your machine and that you have forged it yourself.)

For example, if you have written your bot in python (or pick up one already done bot from this repo, under the `bots` folder for the problem of your interest), then a working plug in could be the following:


```bash
rtal -s wss://ta.di.univr.it/esame  connect -e sum free_sum -- python ~/TALight/example_problems/tutorial/sum/bots/python/sum_mysimplebot.py
```


The `-e` flag at the beginning allows you to assist to the interaction occurring between your bot and the service server. Try omitting it for the service call to proceed silent.


Actually, if you are on Linux/Mac and the python script `free_sum_mysimplebot.py` is given excution permission, as it is the case in the repo you have cloned (again, better cloning than downloading, but you can also assign these permissions with the `chmod` command of the shell), then you could more simply write:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -e sum free_sum -- ~/TALight/example_problems/tutorial/sum/bots/python/sum_mysimplebot.py
```

<details><summary><b>Why the second writing is better and why you can not use it on Windows</b></summary>

This is because only `.exe` files can be executed on Windows, scripts can not (even if their first line is the correct she-bang).

Of course, you can also use the first and longer form of the command also on Linux and Mac, but then it must be the case that the version of python set as default in your current environment is the correct one to run the bot. 
</details>


Try out a few other interactions, like: 

```bash
rtal -s wss://ta.di.univr.it/esame  connect -e -a numbers=big sum free_sum -- ~/TALight/example_problems/tutorial/sum/bots/python/free_sum_mysimplebot.py
```

or:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -a numbers=big -a obj=max_product sum free_sum -- ~/TALight/example_problems/tutorial/sum/bots/python/free_sum_mymaxproductbot.py
```

In all these examples the bot had been written in python, but it could be just any binary with permission to be executed on your local system. For example:

```bash
rtal -s wss://ta.di.univr.it/esame  connect -e sum free_sum -- free_sum_mysimplebot
```

Where the executable binary `free_sum_mysimplebot`, which we assumed to sit in the current directory, could have been obtained by compilation of a source code written in any programming language of your choice like for example C, c++, Rust, or Java.

### To summarize

 With interaction based services the problem solver can make a bot that will conduct that interaction on his behalf. Some interaction based services are meant just for bots.

We suggest you to try out first a simple example service as:

```bash 
rtal -s wss://ta.di.univr.it/esame connect sum free_sum
```

After having experimented with the interaction offered by a service like `free_sum`, connect to it a bot you have in local.   

```bash 
./rtal -s wss://ta.di.univr.it/esame connect -e sum free_sum -- python ~/TALight/example_problems/tutorial/sum/bots/python/free_sum_mysimplebot.py
```


In this way the bot will conduct that same interaction on your behalf and express your competence on the problem. Thanks to the `-e` flag you can observe the dialogue between your bot sitting in local and the service server in the cloud. Here, for this tutorial, you could find the bot `free_sum_mysimplebot.py` among the files of this repo, but the idea is that the problem solver will organize and meta reflect on the involved competences while preparing his own bots. Such a service is meant to offer a convenient way to test the bot and get rich and informative feedback on its behaviuor. This will help to cleanse out the programming bugs at first, but it is meant to assess the competences themselves, and to provide further awareness and challenges. Indeed, the behaviour of most of the services meant for bots can be regulated through arguments which allow the problem solver to set both its own goals and the feedback level he desires from the server. The idea is to let the problem solver authonomously decide when he needs more help or when he does not want to get any spoilering on the problem.  

However, not all TALight services are meant for bots. Indeed, TALight is meant to be used also by problem solvers that do now know how to code and can offer a supportive and entertaining environment also for them. And even problems explicitly addressing coding comptences can comprise a rich set of services meant just for human exploration.

A bot is any automatic system set up by the problem solver. It can be written in any language and then trigger any other software component or library. The problem solver has full control over it since it runs on its local machine.

We assume the bot `sum_mysimplebot.py` run with success, getting positive feedback from the service.
Now, if you run it as follows:

```bash 
rtal -s wss://ta.di.univr.it/esame connect -e -aobj=max_product sum free_sum -- ~/TALight/example_problems/tutorial/sum/bots/python/sum_mysimplebot.py 
```

then the feedback you get should dramatically change since what is required from the bot is different. But you can try out the `sum_mymaxproductbot.py` in the same directory (of this repo that you have cloned in local). 

When you succeed teaching a competence (like when you succeed instructing a bot to do something) then you get confirmed to have acquired that competence in the deep. Therefore, the submission of a bot offers a means to assess the competence. When the service offers you an evaluation on your submissions it confirms you about your advancements and can suggest you further goals and challenges.

