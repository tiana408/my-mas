#!/usr/bin/env python
import sys
from my_mas.crew import MyMasCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'career_preferences': 'QA Analyst, System Engineer, DevOps Engineer, Site Reliability Engineer, Quality Engineer, Test Automation Engineer, Platform Engineer, Infrastructure Engineer, Security Engineer, Cloud Engineer, Technical Project Manager, Product Owner, Scrum Master, Business Systems Analyst, Technical Support Engineer, Release Manager, Configuration Manager',
        'target_industries': [
            'Technology', 'FinTech', 'Healthcare IT', 'Defense Contractors', 'Cybersecurity', 
            'Cloud Services', 'Enterprise Software', 'Federal Government Agencies', 
            'State Government IT Departments', 'Municipal Technology Offices', 
            'Government Research Labs', 'Military Technology Divisions', 
            'Federal Reserve System', 'Government-Sponsored Enterprises'
        ],
        'key_requirements': [
            'Work-Life Balance', 'Salary Range', 'Growth Opportunities', 'Technical Stack',
            'Company Financial Health', 'Stock Performance & Trajectory', 
            'Market Share & Competition Position', 'Funding Status', 'Revenue Growth Rate',
            'Profit Margins', 'Remote Work Policy', 'Healthcare Benefits', 
            'Retirement Benefits', 'Stock Options/RSUs', 'Professional Development Budget',
            'Certification Support', 'Travel Requirements', 'Employee Turnover Rate',
            'Leadership Team Track Record', 'Company Age & Stability', 'Innovation Culture',
            'Work Environment', 'Team Size & Structure', 'Security Clearance Requirements',
            'Regulatory Environment', 'Industry Growth Projections'
        ]
    }
    MyMasCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'career_preferences': 'QA Analyst, System Engineer, DevOps Engineer, Site Reliability Engineer, Quality Engineer, Test Automation Engineer, Platform Engineer, Infrastructure Engineer, Security Engineer, Cloud Engineer, Technical Project Manager, Product Owner, Scrum Master, Business Systems Analyst, Technical Support Engineer, Release Manager, Configuration Manager',
        'target_industries': [
            'Technology', 'FinTech', 'Healthcare IT', 'Defense Contractors', 'Cybersecurity', 
            'Cloud Services', 'Enterprise Software', 'Federal Government Agencies', 
            'State Government IT Departments', 'Municipal Technology Offices', 
            'Government Research Labs', 'Military Technology Divisions', 
            'Federal Reserve System', 'Government-Sponsored Enterprises'
        ],
        'key_requirements': [
            'Work-Life Balance', 'Salary Range', 'Growth Opportunities', 'Technical Stack',
            'Company Financial Health', 'Stock Performance & Trajectory', 
            'Market Share & Competition Position', 'Funding Status', 'Revenue Growth Rate',
            'Profit Margins', 'Remote Work Policy', 'Healthcare Benefits', 
            'Retirement Benefits', 'Stock Options/RSUs', 'Professional Development Budget',
            'Certification Support', 'Travel Requirements', 'Employee Turnover Rate',
            'Leadership Team Track Record', 'Company Age & Stability', 'Innovation Culture',
            'Work Environment', 'Team Size & Structure', 'Security Clearance Requirements',
            'Regulatory Environment', 'Industry Growth Projections'
        ]
    }
    try:
        MyMasCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        MyMasCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'career_preferences': 'QA Analyst, System Engineer, DevOps Engineer, Site Reliability Engineer, Quality Engineer, Test Automation Engineer, Platform Engineer, Infrastructure Engineer, Security Engineer, Cloud Engineer, Technical Project Manager, Product Owner, Scrum Master, Business Systems Analyst, Technical Support Engineer, Release Manager, Configuration Manager',
        'target_industries': [
            'Technology', 'FinTech', 'Healthcare IT', 'Defense Contractors', 'Cybersecurity', 
            'Cloud Services', 'Enterprise Software', 'Federal Government Agencies', 
            'State Government IT Departments', 'Municipal Technology Offices', 
            'Government Research Labs', 'Military Technology Divisions', 
            'Federal Reserve System', 'Government-Sponsored Enterprises'
        ],
        'key_requirements': [
            'Work-Life Balance', 'Salary Range', 'Growth Opportunities', 'Technical Stack',
            'Company Financial Health', 'Stock Performance & Trajectory', 
            'Market Share & Competition Position', 'Funding Status', 'Revenue Growth Rate',
            'Profit Margins', 'Remote Work Policy', 'Healthcare Benefits', 
            'Retirement Benefits', 'Stock Options/RSUs', 'Professional Development Budget',
            'Certification Support', 'Travel Requirements', 'Employee Turnover Rate',
            'Leadership Team Track Record', 'Company Age & Stability', 'Innovation Culture',
            'Work Environment', 'Team Size & Structure', 'Security Clearance Requirements',
            'Regulatory Environment', 'Industry Growth Projections'
        ]
    }
    try:
        MyMasCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")