def get_workday_company_urls() -> dict:
    urls = {
        'NVIDIA': 'https://nvidia.wd5.myworkdayjobs.com/NVIDIAExternalCareerSite?jobFamilyGroup=0c40f6bd1d8f10ae43ffaefd46dc7e78',
        'SALESFORCE': 'https://salesforce.wd12.myworkdayjobs.com/en-US/External_Career_Site/details/Lead-Marketing-Cloud-Solution-Engineer_JR268932?jobFamilyGroup=14fa3452ec7c1011f90d0002a2100000',
        'RED_HAT': 'https://redhat.wd5.myworkdayjobs.com/Jobs',
        'CROWDSTRIKE': 'https://crowdstrike.wd5.myworkdayjobs.com/crowdstrikecareers'
    }
    return urls

def get_workday_post_time_range() -> list[str]:
    return ['posted today', 'posted yesterday', 'posted 2 days ago', 'posted 3 days ago',
     'posted 4 days ago', 'posted 5 days ago', 'posted 6 days ago', 'posted 7 days ago']

