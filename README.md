# Take Home Engineering Challenge

We are a very practical team at Microsoft and this extends to the way that we work with you to find out if this team is a great fit for you. We want you to come away with a great understanding of the work that we actually do day to day and what it is like to work with us.

So instead of coding at a whiteboard with someone watching over your shoulder under high pressure, which is not a thing we often do, we instead discuss code that you have written previously when we meet.

This can be a project of your own or a substantial pull request on a third party project, but some folks have done largely private or proprietary work, and this engineering challenge is for you.

## Guidelines

-   This is meant to be an assignment that you spend approximately three hours of dedicated, focused work. Do not feel like you need to overengineer the solution with dozens of hours to impress us. Be biased toward quality over quantity.

-   Think of this like an open source project. Create a repo on Github, use git for source control, and use README.md to document what you built for the newcomer to your project.

-   Our team builds, alongside our customers and partners, systems engineered to run in production. Given this, please organize, design, test, deploy, and document your solution as if you were going to put into production. We completely understand this might mean you can't do as much in the time budget. Be biased for production-ready over features.

-   Think out loud in your submission's documentation. Document tradeoffs, the rationale behind your technical choices, or things you would do or do differently if you were able to spend more time on the project or do it again.

-   Our team meets our customers where they are in terms of software engineering platforms, frameworks, tools, and languages. This means you have wide latitude to make choices that express the best solution to the problem given your knowledge and favorite tools. Make sure to document how to get started with your solution in terms of setup.

## The Problem

Getting around large cities can be quite a hassle, and New York City is no exception. One thing that helps, is being able to predict how long a trip might take and how much that trip might cost. Luckily, NYC provides public data about transportation which includes all of the metrics we need!

Your assignment, is to help us quickly look at transportation fare data for tips between different boroughs in NYC so that when we travel there, it is easier for us to get around.

This is a freeform assignment. You can write a web API that returns a set of trip metrics. You can write a web frontend that visualizes the trips and shows cheapest/fastest options. We also spend a lot of time in the shell, so a CLI that gives us a few options would be great. And don't be constrained by these ideas if you have a better one!

The only requirements for the assignment are:

1. We can filter based on yellow cab, green cab, and for-hire vehicle.
2. We can provide a start and end borough for our trip.
3. We can filter based on datetime.
4. The returned data shows some interesting metrics that will help us get around.
5. Your code is well-tested.
6. Documentation is provided for how to build and run your code.

Feel free to tackle this problem in a way that demonstrates your expertise of an area -- or takes you out of your comfort zone. For example, if you build Web APIs by day and want to build a frontend to the problem or a completely different language instead, by all means go for it - learning is a core competency in our group. Let us know this context in your solution's documentation.

New York City transportation data is [located here](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page). We've included a copy of the [Jan 2018 data](https://cseboulderinterview.blob.core.windows.net/triprecord/tripdata.zip) as well.

Good luck! Please send a link to your solution on Github before the day of your interview so we can review it.
