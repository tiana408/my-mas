from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment and import any custom tools if needed
# from my_mas.tools.custom_tool import MyCustomTool
# from crewai_tools import SerperDevTool

@CrewBase
class MyMasCrew():
    """Multi-Agent System for Career Exploration"""

    @agent
    def career_analyst(self) -> Agent:
        """Creates the Career Analyst Agent for defining career exploration framework"""
        return Agent(
            config=self.agents_config['career_analyst'],
            verbose=True
            # Uncomment and add tools if needed
            # tools=[...]
        )

    @agent
    def market_researcher(self) -> Agent:
        """Creates the Market Researcher Agent for industry data collection"""
        return Agent(
            config=self.agents_config['market_researcher'],
            verbose=True
            # Uncomment and add tools if needed
            # tools=[...]
        )

    @agent
    def requirements_analyst(self) -> Agent:
        """Creates the Requirements Analyzer Agent for synthesizing job requirements"""
        return Agent(
            config=self.agents_config['requirements_analyzer'],
            verbose=True
            # Uncomment and add tools if needed
            # tools=[...]
        )

    @agent
    def career_advisor(self) -> Agent:
        """Creates the Career Advisor for generating recommendations"""
        return Agent(
            config=self.agents_config['career_advisor'],
            verbose=True
            # Uncomment and add tools if needed
            # tools=[...]
        )

    @task
    def career_analyst_task(self) -> Task:
        """Creates the Career Analysis Task for defining exploration framework"""
        return Task(
            config=self.tasks_config['career_analysis_task'],
        )

    @task
    def market_researcher_task(self) -> Task:
        """Creates the Market Research Task for collecting industry data"""
        return Task(
            config=self.tasks_config['market_research_task'],
        )

    @task
    def requirements_analyst_task(self) -> Task:
        """Creates the Requirements Analysis Task for synthesizing findings"""
        return Task(
            config=self.tasks_config['requirements_analysis_task'],
        )

    @task
    def career_advisor_task(self) -> Task:
        """Creates the Career Advisory Task for generating final recommendations"""
        return Task(
            config=self.tasks_config['career_advisory_task'],
            output_file='career_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Career Exploration Crew with sequential processing"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )