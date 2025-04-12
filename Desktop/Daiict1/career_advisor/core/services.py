import os
import requests
import json
from groq import Groq


class CareerAdvisorService:
    def __init__(self):
        # Initialize Groq client with API key
        # You'll need to set this in your environment variables
        api_key = os.environ.get("GROQ_API_KEY", "your-groq-api-key")
        self.client = Groq(api_key=api_key)
        
        # Basic sample data (could be replaced with database queries)
        self.career_data = {
            "coding + design": ["Frontend Developer", "UI/UX Designer", "Web Developer"],
            "analytics + logic": ["Data Analyst", "Business Analyst", "Product Manager"],
            "helping + teaching": ["Teacher", "Career Counselor", "HR Specialist"]
        }
    
    def get_career_paths(self, interest):
        for key in self.career_data:
            if interest.lower() in key:
                return self.career_data[key]
        return ["Try exploring new skills or talking to a career counselor."]
    
    def ask_groq(self, user_prompt, feature="general"):
        system_message = "You are a helpful AI career advisor chatbot."

        if feature == "resume":
            system_message = "You are an expert resume reviewer and ATS score to resume."
        elif feature == "interview":
            system_message = "You are an expert career coach for interview preparation."
        elif feature == "college":
            system_message = "You give guidance about college majors and career alignment."

        try:
            chat_completion = self.client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"Error while getting AI response: {str(e)}"
    
    def get_career_advice(self, question):
        """
        Generate career advice using Groq AI
        """
        try:
            prompt = f"""
            As a career advisor, please provide helpful, accurate, and insightful advice to the following career-related question. 
            Focus on practical steps, skill development, and actionable insights.
            
            Question: {question}
            """
            
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert career advisor with deep knowledge of various industries, job markets, skills, and educational pathways."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="mixtral-8x7b-32768",
                max_tokens=800,
                temperature=0.7,
            )
            
            return completion.choices[0].message.content
        except Exception as e:
            # Fallback response in case of API failure
            return f"I'm sorry, I couldn't generate advice at the moment. Please try again later. Error: {str(e)}"


def get_career_advice(question):
    """
    Get career advice from Grok AI
    
    This is a simulated implementation since we don't have direct API access to Grok.
    In a real implementation, you would use the appropriate Grok API client.
    """
    try:
        # Simulate a Grok AI response for different career questions
        question_lower = question.lower()
        
        # For software development careers
        if any(term in question_lower for term in ['software', 'programming', 'developer', 'coding']):
            return {
                "success": True,
                "response": """
# Software Development Career Path

Software development is a dynamic field that involves designing, building, and maintaining applications, systems, and services.

## Required Skills:
1. **Programming Languages**: Proficiency in languages like Python, JavaScript, Java, C#, or Go
2. **Data Structures & Algorithms**: Understanding of fundamental computer science concepts
3. **Version Control**: Experience with Git and GitHub
4. **Testing & Debugging**: Ability to write clean, testable code
5. **Problem-Solving**: Strong analytical thinking and troubleshooting skills

## Career Progression:
- **Junior Developer** (0-2 years): Learning foundations, working on supervised tasks
- **Mid-level Developer** (2-5 years): Taking ownership of features, mentoring juniors
- **Senior Developer** (5+ years): Architecture design, technical leadership, complex problem-solving
- **Lead Developer/Architect**: System design, technical vision, team leadership
- **Engineering Manager/CTO**: Strategic technical direction, organizational leadership

## Industry Outlook:
- Average starting salary: $70,000-$90,000
- Senior-level salary range: $120,000-$200,000+
- Job growth projected at 22% through 2030 (much faster than average)
- Remote work opportunities abundant

## Educational Paths:
- Computer Science degree (traditional route)
- Coding bootcamps (accelerated learning)
- Self-taught with portfolio projects
- Online courses & certifications (Udemy, Coursera, etc.)

## Advice for Success:
1. Build a strong portfolio on GitHub
2. Contribute to open-source projects
3. Develop soft skills (communication, teamwork)
4. Practice continuous learning - technology evolves rapidly
5. Specialize in an area that interests you (web, mobile, AI, etc.)
                """
            }
            
        # For data science careers
        elif any(term in question_lower for term in ['data science', 'data analyst', 'machine learning', 'ai']):
            return {
                "success": True,
                "response": """
# Data Science Career Path

Data Science combines statistics, mathematics, programming, and domain expertise to extract meaningful insights from data.

## Required Skills:
1. **Programming**: Python or R proficiency
2. **Statistics & Mathematics**: Strong foundation in statistical methods, linear algebra, and calculus
3. **Data Manipulation**: SQL, pandas, and data wrangling expertise
4. **Machine Learning**: Understanding of ML algorithms and frameworks
5. **Data Visualization**: Ability to create clear, impactful visualizations
6. **Domain Knowledge**: Understanding of the specific industry you work in

## Career Progression:
- **Data Analyst** (Entry level): Reporting, basic analysis, visualization
- **Junior Data Scientist** (0-2 years): Building models with supervision, data preprocessing
- **Data Scientist** (2-5 years): Developing complex models, feature engineering, project ownership
- **Senior Data Scientist** (5+ years): Solving novel problems, setting methodology standards
- **Principal Data Scientist/ML Engineer**: Architecture design, advanced research, team leadership
- **Chief Data Officer/Director of Data Science**: Strategic direction, organizational leadership

## Industry Outlook:
- Average starting salary: $85,000-$110,000
- Senior-level salary range: $130,000-$180,000+
- Job growth projected at 31% through 2030
- High demand across all industries (finance, healthcare, tech, retail)

## Educational Paths:
- Master's or PhD in Computer Science, Statistics, Mathematics, or related field
- Bachelor's degree plus specialized bootcamps
- Online specializations (Coursera, edX)
- Industry certifications (TensorFlow, AWS, Azure)

## Advice for Success:
1. Build a portfolio of projects that demonstrate your skills
2. Participate in Kaggle competitions
3. Develop strong communication skills to explain complex concepts
4. Stay current with research and emerging technologies
5. Network with professionals in the field
6. Consider specializing in a specific domain (NLP, computer vision, etc.)
                """
            }
            
        # For UX/UI design careers
        elif any(term in question_lower for term in ['design', 'ux', 'ui', 'user experience']):
            return {
                "success": True,
                "response": """
# UX/UI Design Career Path

UX/UI design focuses on creating intuitive, efficient, and enjoyable digital experiences for users.

## Required Skills:
1. **User Research**: Understanding user needs and behaviors
2. **Wireframing & Prototyping**: Creating mockups with tools like Figma, Sketch, or Adobe XD
3. **Visual Design**: Typography, color theory, and layout principles
4. **Interaction Design**: Creating intuitive user flows and interactions
5. **Usability Testing**: Evaluating designs with real users

## Career Progression:
- **Junior UX/UI Designer** (0-2 years): Working on specific components, learning methodologies
- **UX/UI Designer** (2-4 years): Creating full user experiences, research to implementation
- **Senior UX/UI Designer** (4+ years): Leading design initiatives, mentoring juniors
- **Lead Designer/Design Manager**: Team leadership, design systems, strategic direction
- **Design Director/VP of Design**: Organizational leadership, design culture

## Industry Outlook:
- Average starting salary: $65,000-$85,000
- Senior-level salary range: $100,000-$150,000+
- Job growth projected at 13% through 2030
- Increasing emphasis on digital experiences across all industries

## Educational Paths:
- Bachelor's degree in Design, HCI, or related field
- UX/UI bootcamps (General Assembly, Designlab)
- Self-taught with a strong portfolio
- Online courses and certifications

## Advice for Success:
1. Build a comprehensive portfolio showing your process and solutions
2. Develop storytelling skills to present your work effectively
3. Learn basic front-end coding (HTML, CSS) to better collaborate with developers
4. Stay current with design trends and user expectations
5. Practice empathy and understanding diverse user needs
6. Network within the design community (Dribbble, Behance)
                """
            }
        
        # For cybersecurity careers
        elif any(term in question_lower for term in ['security', 'cyber', 'cybersecurity', 'hacking']):
            return {
                "success": True,
                "response": """
# Cybersecurity Career Path

Cybersecurity focuses on protecting systems, networks, and data from digital attacks and unauthorized access.

## Required Skills:
1. **Network Security**: Understanding of protocols, architecture, and security controls
2. **Operating Systems**: Deep knowledge of Windows, Linux, and other systems
3. **Programming**: Scripting (Python, Bash) and understanding of secure coding practices
4. **Security Tools**: Proficiency with vulnerability scanners, SIEM systems, and penetration testing tools
5. **Risk Assessment**: Ability to identify, analyze, and prioritize security threats

## Career Progression:
- **Security Analyst** (Entry level): Monitoring, incident response, implementing controls
- **Security Engineer** (2-4 years): Building and maintaining security infrastructure
- **Penetration Tester/Ethical Hacker**: Identifying vulnerabilities through controlled attacks
- **Security Architect** (5+ years): Designing secure systems and infrastructure
- **CISO (Chief Information Security Officer)**: Executive leadership, security strategy

## Industry Outlook:
- Average starting salary: $75,000-$90,000
- Senior-level salary range: $120,000-$200,000+
- Job growth projected at 33% through 2030 (much faster than average)
- Persistent shortage of qualified professionals

## Educational Paths:
- Bachelor's in Cybersecurity, Computer Science, or IT
- Military or government security experience
- Industry certifications (CISSP, CEH, Security+, OSCP)
- Specialized bootcamps and training programs

## Advice for Success:
1. Pursue relevant certifications for your specialization
2. Build a home lab for hands-on practice and experimentation
3. Stay current with emerging threats and countermeasures
4. Develop problem-solving and analytical thinking skills
5. Understand business context and communicate security needs effectively
6. Practice ethical responsibility and integrity
                """
            }
            
        # For business/management careers
        elif any(term in question_lower for term in ['business', 'management', 'leadership', 'mba']):
            return {
                "success": True,
                "response": """
# Business Management Career Path

Business management involves planning, organizing, directing, and controlling organizational resources to achieve objectives efficiently and effectively.

## Required Skills:
1. **Leadership**: Ability to inspire, motivate, and guide teams
2. **Strategic Thinking**: Long-term planning and vision development
3. **Financial Acumen**: Understanding budgets, forecasting, and financial statements
4. **Communication**: Clear, effective communication with diverse stakeholders
5. **Problem-Solving**: Analytical and creative approaches to business challenges
6. **Adaptability**: Flexibility in changing market conditions

## Career Progression:
- **Team Lead/Supervisor** (Entry level): First-line management, operational oversight
- **Manager** (3-5 years): Department or functional area responsibility
- **Senior Manager/Director** (5-10 years): Strategy implementation, cross-functional leadership
- **Vice President/Executive**: Organizational strategy, substantial P&L responsibility
- **C-Suite (CEO, COO, etc.)**: Enterprise leadership, vision-setting, ultimate accountability

## Industry Outlook:
- Average starting salary: $60,000-$85,000
- Senior-level salary range: $120,000-$250,000+
- Job growth varies by industry, with healthcare and tech management growing fastest
- Increasing demand for digital transformation leadership

## Educational Paths:
- Bachelor's degree in Business, Management, or related field
- MBA or specialized master's degree
- Professional certifications (PMP, Lean Six Sigma)
- Executive education programs

## Advice for Success:
1. Develop both technical expertise and people skills
2. Seek mentorship from experienced leaders
3. Gain experience across multiple business functions
4. Build a strong professional network
5. Develop emotional intelligence and cultural awareness
6. Commit to continuous learning and adaptability
7. Practice ethical leadership and integrity
                """
            }
        
        # Default response for other career questions
        else:
            return {
                "success": True,
                "response": """
# Career Development Guidance

Thank you for your career question. Here are some general principles for career development across fields:

## Key Elements of Career Success:

### 1. Self-Assessment
- **Skills Inventory**: Identify your technical and transferable skills
- **Interest Assessment**: Determine what truly engages and motivates you
- **Values Clarification**: Understand what matters most to you in work
- **Personality Fit**: Consider how your traits align with different environments

### 2. Education & Skill Development
- **Formal Education**: Degrees and certificates relevant to your field
- **Continuing Education**: Ongoing learning to stay current
- **Skill-Based Training**: Focused development of specific competencies
- **Experiential Learning**: Internships, projects, and practical experience

### 3. Strategic Planning
- **Goal Setting**: Clear short and long-term career objectives
- **Action Planning**: Specific steps to achieve your goals
- **Timeline Development**: Realistic schedules for career milestones
- **Adaptability**: Flexibility to adjust as circumstances change

### 4. Professional Networking
- **Relationship Building**: Meaningful connections in your field
- **Digital Presence**: Professional profiles and online engagement
- **Mentorship**: Guidance from experienced professionals
- **Industry Involvement**: Participation in relevant associations and events

### 5. Experience Building
- **Progressive Responsibility**: Increasing scope and authority
- **Project Diversity**: Varied experiences to broaden skills
- **Achievement Documentation**: Tracking accomplishments and results
- **Leadership Development**: Opportunities to guide and influence others

### Universal Career Advice:
1. **Research thoroughly** before committing to a field
2. **Start with fundamentals** and build specialized knowledge
3. **Create tangible examples** of your capabilities
4. **Develop communication skills** regardless of your field
5. **Build relationships** with colleagues and industry peers
6. **Embrace continuous learning** as technologies and practices evolve
7. **Balance specialization** with adaptable, transferable skills

For more specific guidance, please provide details about which particular career field interests you.
                """
            }
            
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }