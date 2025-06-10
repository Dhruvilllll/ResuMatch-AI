def resume_analysis_prompt(resume_text, jd_text):
    """
    Generates a prompt to send to the LLM for analyzing resume vs job description.
    Returns a structured comparison prompt.
    """
    return f"""
You are an experienced HR recruiter and AI assistant. Your task is to compare a RESUME with a JOB DESCRIPTION and evaluate the job fit.

### RESUME:
{resume_text}

### JOB DESCRIPTION:
{jd_text}

Please return the following:

1. ✅ Match Score (0–100%)
2. ✅ List of Matching Skills and Technologies
3. ❌ List of Missing Skills or Experience
4. 💡 Actionable Suggestions to Improve the Resume
5. Summary: Is this candidate a good fit? Why or why not?

Respond in a clear, structured format with bullet points or sections.
"""
