# Summary

Created by dbulysse (Ben Pence)

_restraint_ is a command line tool that, given (1) a history of which days you performed some activity and (2) how many times per period of time you would like to perform that activity, will tell you whether you should "do it" today or "don't do it".

# How To Use

For now, the history of activity is simply a plaintext file in the format:

    2013/12/25
    2013/12/26
    2013/12/28

And you specify how often you would like to perform an activity in the form 'X times per Y days/weeks/months/years':

    $ restraint test activity.log 4 6 weeks
    Do it
    $ restraint test activity.log 3 6 weeks
    Don't do it

which can be interpreted as "given my activity.log, can I perform the activity if I wish to do it no more than 4 times in the last 6 weeks?"

You can mark today's date for performingas to the log

    $ restraint mark activity.log 

Or add a specific date to the log:

    $ restraint mark activity.log 2014/03/27

# Example Use Cases

* You wish to reduce how much you consume alcohol to twice per month: `restraint test drinking.log 2 1 months`
* You wish to reduce how much meat you consume to 2 days per week:    `restraint test meat.log 2 1 weeks`
* You wish to send out an email on a mailing list 4 times per year:   `restraint test mail.log 1 4 months`

# Future Development

* _restraint_ should be aware of leap year when you specify "months" or "years"
* _restraint_ should implement more types of restraints and allow 'and','or' type combining
