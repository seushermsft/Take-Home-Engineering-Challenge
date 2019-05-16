# Take Home Engineering Challenge

## triphelper.nyc

I am going to use Ruby and Rails on this project due to the extreme time constraint. Rails will allow me to leverage a ton of web application convention to speed up my development. However, 3 hours is not much time to put all the skills I've gained over the past 8 years on display. As such, I am going to relax these of my development processies for this challenge:

- Third party code should be audited for activity, number of issues and any of _their_ dependancies to determine project health before including them in your own work
  - Gems will not be scrutinized as hard as if this was a real project
- Rubocop is a great tool to enforce consistent style across the project without taking time away from constructive code review
  - Complexity metrics will be disabled to save time

However, in this project I am still aiming to provide:

- Clear, consistent, commented and DRY code
- A functional interface
- Reasonable code coverage
- CI

## Setup

- Clone repository
- Install bundler

```bash
$ bundle install
$ rails db:create db:setup
```

## Run

### Application

```bash
$ rails s
```

### Testing

```bash
$ rubocop
$ brakeman
$ rails test
$ rails test:system
```

Running the system tests on a Windows (WSL) machine requires a little bit of hoop jumping:
- Comment out webdrivers in Gemfile
- - The WSL is a little too good at hiding the fact that we're on windows, so it's a difficult to detect inside the gemfile. Thinking about it now I wonder if we could look for a windows specific file on the FS to detect this.
- Follow [This](http://ngauthier.com/2017/09/rails-system-tests-with-headless-chrome-on-windows-bash-wsl.html)
