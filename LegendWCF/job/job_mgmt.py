import apscheduler.job
import apscheduler.schedulers
import apscheduler.schedulers.background
from apscheduler.triggers.cron import CronTrigger
import time
import apscheduler
from typing import Any, Callable
from datetime import datetime, timedelta, timezone

class LegendJob(apscheduler.schedulers.background.BackgroundScheduler):
    '''微信机器人定时任务管理
    '''
    def __init__(self, gconfig=..., **options):
        super().__init__(gconfig, **options)
    
    def one_time_job(self, func: Callable, microseconds: int = 0, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, months: int = 0, years: int = 0, timedelta_: timedelta = None, datetime_: datetime | str = None,id: Any = None, name: Any = None, args: Any = None, kwargs: Any = None, **trigger_args: Any) -> apscheduler.job.Job | int:
        '''仅执行一次的任务

        time_>timedelta_>microseconds~years

        Args:
            timedelta_: 过多久执行, timedelta精确时间间隔
            time_: 执行时间, datetime精确时间或类似'YYYY-MM-DD HH:MM:SS'的字符串形式
        
        Returns:
            运行正常则返回Job类型对象, 表示添加的任务

            返回0代表任务与现在间隔太短或是过去时间
        '''
        if datetime_:
            return self.add_job(func, 'date', run_date=datetime_, name=name, id=id, args=args, kwargs=kwargs, **trigger_args)
        elif timedelta_:
            now = datetime.now()
            if timedelta_.total_seconds <= 3:
                return 0
            run = now + timedelta_
            return self.add_job(func, 'date', run_date=run, name=name, id=id, args=args, kwargs=kwargs, **trigger_args)
        else:
            now = datetime.now()
            add = timedelta(year=years, month=months, day=days, hour=hours, minute=minutes, second=seconds, microsecond=microseconds)
            if add.total_seconds <= 3:
                return 0
            run = now + add
            return self.add_job(func, 'date', run_date=run, name=name, id=id, args=args, kwargs=kwargs, **trigger_args)
    
    def interval_job(self, func: Callable, microseconds: int = 0, seconds: int = 0, minutes: int = 0, hours: int = 0, days: int = 0, weeks: int = 0, timedelta_: timedelta = None,jitter: int = 0, id: Any = None, name: Any = None, args: Any = None, kwargs: Any = None, **trigger_args: Any) -> apscheduler.job.Job:
        '''周期执行的任务

        timedelta_>microseconds~years

        Args:
            jitter: 振动参数, 在每次执行前随机添加随机浮动的秒数
            timedelta_: 每过多久执行, timedelta精确时间间隔
        
        Returns:
            Job类型对象, 表示添加的任务
        '''
        if timedelta_:
            return self.add_job(func, 'interval', seconds=timedelta_.total_seconds(), name=name, id=id, jitter=jitter, args=args, kwargs=kwargs, **trigger_args)
        else:
            timedelta_ = timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds)
            return self.add_job(func, 'interval', seconds=timedelta_.total_seconds(), name=name, id=id, jitter=jitter, args=args, kwargs=kwargs, **trigger_args)
    
    def cron_job(self, func: Callable, year=None, month=None, day=None, week=None, day_of_week=None, hour=None, minute=None,second=None, start_date=None, end_date=None, timezone: timezone=timezone(timedelta(hours=8), name='Asia/Shanghai'), jitter=None, standard_cron: str = None, id: Any = None, name: Any = None, args: Any = None, kwargs: Any = None, **trigger_args: Any) -> apscheduler.job.Job:
        '''cron任务

        具体参数格式请参照官方CronTrigger类, ConTrigger优先
        Args:
            int|str year: 4-digit year
            int|str month: month (1-12)
            int|str day: day of month (1-31)
            int|str week: ISO week (1-53)
            int|str day_of_week: number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
            int|str hour: hour (0-23)
            int|str minute: minute (0-59)
            int|str second: second (0-59)
            datetime|str start_date: earliest possible date/time to trigger on (inclusive)
            datetime|str end_date: latest possible date/time to trigger on (inclusive)
            datetime.tzinfo|str timezone: time zone to use for the date/time calculations (defaults
                to scheduler timezone)
            jitter: delay the job execution by ``jitter`` seconds at most

            note: The first weekday is always **monday**.

            standard_cron: 可直接传入CronTrigger表达式
        Returns:
            Job类型对象, 表示添加的任务
        '''
        if standard_cron:
            return self.add_job(func, CronTrigger.from_crontab(standard_cron), id=id, name=name, args=args, kwargs=kwargs, **trigger_args)
        else:
            return self.add_job(func, 'cron', year=year, month=month, day=day, hour=hour, minute=minute, second=second, day_of_week=day_of_week, start_date=start_date, end_date=end_date, timezone=timezone, jitter=jitter, id=id, name=name, args=args, kwargs=kwargs, **trigger_args)

if __name__ == '__main__':
    
    def p(c):
        print(c)
    l = LegendJob({'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    }})
    l.cron_job(func=p, second='*', day_of_week='sat', args=['nihao'])
    l.start()
    while 1:
        time.sleep(1)