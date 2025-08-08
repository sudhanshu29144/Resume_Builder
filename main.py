from fastapi import FastAPI ,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
from fastapi.responses import FileResponse

app = FastAPI()
# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/" ,response_class=HTMLResponse)
def resume_form():
      html="""
      <html>
            <head>
                  <title>Resume Form</title>
                  <style>
                        body {
                              font-family: sans-serif;
                              background-color: #E1EBEE;
                              padding: 50px;
                        }

                        .form-container {
                              max-width: 800px;
                              margin: auto;
                              background: blur;
                        
                              
                              padding: 30px;
                              border-radius: 10px;
                              box-shadow: 0 8px 20px rgba(0,0,0,0.08);
                              
                              }

                        h1 {
                              text-align: center;
                              color: linear-gradient(to right, #1d3557, #457b9d);
                              margin-bottom: 20px;
                              }

                        h4 {
                              margin-top: 20px;
                              font-size: 16px;
                              color: #1d3557;
                              }

                        input, textarea {
                              width: 100%;
                              padding: 10px;
                              margin-top: 6px;
                              margin-bottom: 20px;
                              font-size: 16px;
                              border: none;
                              border-bottom: 2px solid grey;
                              background: transparent;
                              border-radius: 4px;
                              }

                        textarea {
                              resize: vertical;
                              }

                        button[type="submit"] {
                              background-color: grey;
                              color: white;
                              padding: 12px 24px;
                              font-size: 16px;
                              font-weight: bold;
                              border: none;
                              border-radius: 6px;
                              cursor: pointer;
                              transition: background 0.3s ease;
                              margin-top: 30px;
                              display: block;
                             
                              width: fit-content;
                              margin: 30px auto 0;

                              }
                        button[type="submit"]:hover {
                              background-color: green;
                              }
            
                  </style>
            </head>
            <body>
            <div class="form-container">
                  <h1>Resume Form</h1>
                  <form action="/resume_preview" method="post">
                        <h4>Name:</h4>
                        <input name="name" type="text" placeholder="Name" required>
                        <h4>E-mail:</h4>
                        <input name="email" type="email" placeholder="Email" required>
                        <h4>Phone.No.</h4>
                        <input name="phone" type="tel" placeholder="Phone Number" required>
                        <h4>Summary</h4>
                        <textarea name="summary" type="text" placeholder="Summary"></textarea><br><br>
                        <h4>Education</h4>
                        <h5>Postgraduate</h5>
                        <input name="pg_degree" type="text" placeholder="Pg. Deg. Name">
                        <input name="pg_institute" type="text" placeholder="Institute Name">
                        <input name="pg_marks" type="int" placeholder="Marks">
                        <input name="pg_year" type="text" placeholder="Passing Year"><br><br>
                        
                        <h5>Graduate</h5>
                        <input name="grad_degree" type="text" placeholder="Gra. Deg. Name">
                        <input name="grad_institute" type="text" placeholder="Institute Name">
                        <input name="grad_marks" type="int" placeholder="Marks">
                        <input name="grad_year" type="text" placeholder="Passing Year"><br><br>
                        
                        <h5>Intermediate</h5>
                        
                        <input name="class12_board" type="text" placeholder="Board Name">
                        <input name="class12_school" type="text" placeholder="Institute Name">
                        <input name="class12_marks" type="int" placeholder="Marks">
                        <input name="class12_year" type="text" placeholder="Passing Year"><br><br>
                        
                        <h5>Matriculation</h5>
                        
                        <input name="class10_board" type="text" placeholder="Board Name">
                        <input name="class10_school" type="text" placeholder="Institute Name">
                        <input name="class10_marks" type="int" placeholder="Marks">
                        <input name="class10_year" type="text" placeholder="Passing Year"><br><br>
                        
                        <h4>Skills</h4>
                        <input name="skills" type="text" placeholder="Skills"><br><br>
                        <input name="frontend" type="text" placeholder="Frontend Skills"><br><br>
                        <input name="backend" type="text" placeholder="Backend Skills"><br><br>
                        <input name ="database" type="text" placeholder="Database Skills"><br><br>
                        <input name="framework" type="text" placeholder="Framework Skills"><br><br>
                        
                        <h4>Experience</h4>
                        <input name="job_title" type="text" placeholder="Job Title"><br><br>
                        <input name="company_name" type="text" placeholder="Company Name"><br><br>
                        <input name="job_duration" type="text" placeholder="Job Duration"><br><br>
                        <textarea name="job_description" type="text" placeholder="Job Description" rows="4"></textarea><br><br>

                        <h4>Project</h4>
                        <input name="project_title" type="text" placeholder="Project Title">
                        <textarea name="description" type="text" row="3" placeholder="Description"></textarea>
                        <input name="tech_use" type="text" placeholder="Technology Used">
                        
                        
                        <h4>Certification</h4>
                        <input name="cert_name" type="text" placeholder="Certification Name">
                        <input name="cert_institute" type="text" placeholder="Certification Institute">
                        <input name="cert_year" type="text" placeholder="Certification Year"><br><br>
                        <button type="submit">Submit</button>
                        </div>
                  </form>
            </body>
      </html>
      """    
      return HTMLResponse(content=html)

@app.post("/resume_preview", response_class=HTMLResponse)    
def resume_preview(
      name: str= Form (...), 
      email: str = Form (...),
      phone: int = Form(...),
      summary: str = Form(...),
      #education
      pg_degree: str =Form(None),
      pg_institute: str = Form(None),
      pg_marks: str = Form(None),
      pg_year: str = Form(None),
      
      grad_degree: str =Form(None),
      grad_institute: str = Form(None),
      grad_marks: str = Form(None),
      grad_year: str = Form(None),
      
      
      class12_board: str = Form(None),
      class12_school: str =Form(None),
      class12_marks: str = Form(None),
      class12_year: str = Form(None),
      
      class10_board: str =Form(None),
      class10_school: str = Form(None),
      class10_marks: str = Form(None),
      class10_year: str = Form(None),

      skills: str =Form(...),
      frontend: str = Form(...),
      backend : str = Form(...),
      framework : str = Form(...),
      database: str = Form(...),
      
      job_title: str = Form(None),
      company_name: str = Form(None),
      job_duration: str = Form(None),
      job_description: str = Form(None),
      
      project_title: str = Form(None),
      description: str = Form(None),
      tech_use:  str = Form(None),
      
      cert_name: str = Form(None),
      cert_institute: str = Form(None),
      cert_year: str = Form(None),
):
      skills_html = " "
      if skills or frontend or backend or database or framework :
            skills_html += f"<h3>Skills</h3>"
      

      if skills.strip():
            skills_html += f"<p><strong>General:</strong> {skills}</p>"
      if frontend.strip():
            skills_html += f"<p><strong>Frontend:</strong> {frontend}</p>"
      if backend.strip():
            skills_html += f"<p><strong>Backend:</strong> {backend}</p>"
      if database.strip():
            skills_html += f"<p><strong>Database:</strong> {database}</p>"
      if framework.strip():
            skills_html += f"<p><strong>Framework:</strong> {framework}</p>"
      
      education_html = " "
      if pg_degree or grad_degree or class12_board or class10_board :
            education_html +=f"<h3>Education</h3>"

      if pg_degree or pg_institute or pg_marks or pg_year :
            education_html += f"""
                  <div class="edu-row">
                  <span class="college-name">{(pg_institute or '—').upper()}</span>
                  <span class="passing-year">({pg_year or '—'})</span>
                  </div>

                  <p class="course-title">{(pg_degree or '—').upper()}</p>
                  <p>Marks: {pg_marks or '-'}</p>
                  """


      if grad_degree or grad_institute or grad_marks or grad_year:
            education_html += f"""
                  <div class="edu-row">
                  <span class="college-name">{(grad_institute or '—').upper()}</span>
                  <span class="passing-year">({grad_year or '—'})</span>
                  </div>

                  <p class="course-title">{(grad_degree or '—').upper()}</p>
                  <p>Marks: {grad_marks or '-'}</p>
                  """
      if class12_board or class12_school or class12_marks or class12_year:
            education_html += f"""
                  <div class="edu-row">
                  <span class="college-name">{(class12_school or '—').upper()}</span>
                  <span class="passing-year">({class12_year or '—'})</span>
                  </div>

                  <p class="course-title">{(class12_board or '—').upper()}</p>
                  <p>Marks: {class12_marks or '-'}</p>
                  """

      if class10_board or class10_school or class10_marks or class10_year:
            education_html += f"""
                  <div class="edu-row">
                  <span class="college-name">{(class10_school or '—').upper()}</span>
                  <span class="passing-year">({class10_year or '—'})</span>
                  </div>

                  <p class="course-title">{(class10_board or '—').upper()}</p>
                  <p>Marks: {class10_marks or '-'}</p>
                  """

      experience_html = " "

      if job_title or company_name or job_duration or job_description:
            experience_html = "<h3>Experience</h3>"
            
            experience_html += f"""
                  <div class="edu-row">
                  <span class="college-name">{(company_name or '—').upper()}</span>
                  <span class="passing-year">({job_duration or '—'})</span>
                  </div>

                  <p class="course-title">{(job_title or '—').upper()}</p>
                  <p> {job_description or '-'}</p>
                  """
      project_html =" "
      if project_title or description or tech_use:
            project_html ="<h3>Project</h3>"
            project_html +=f"<p><strong>{(project_title or '-').upper()}</strong><br> {description or '-'} <br><strong>Technology Use:</strong>{tech_use or '-'}</p> "
            
            
      certification_html = " "
      if cert_name or cert_institute or cert_year:
            certification_html = "<h3>Certification</h3>"
            certification_html += f"<p>{cert_name or '—'} <strong> ({cert_institute or '—'})</strong> <br><em>Year:{cert_year or '—'}</em></p>"
           
            
            
      summary_html = ""
      if summary.strip():
            summary_html = f"""
                  <h3>Summary:</h3>
                  <p><em>{summary}</em></p>
                  <hr>
            """

      html = f"""
      <html>
      <head>
            <title>{name}'s Resume</title>
            <style>
                  body {{
                        background: linear-gradient(to right, #f4f4f4, #eaeaea);
                        font-family: 'Segoe UI', sans-serif;
                        padding: 50px;
                  }}

                  .resume-container {{
                        max-width: 800px;
                        margin: auto;
                        background: #ffffff;
                        padding: 30px 40px;
                        border-radius: 12px;
                        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
                        font-family: 'Segoe UI', sans-serif;
                  }}

                  h2 {{
                        text-align: center;
                        color: grey;
                        font-size: 38px;
                        margin-bottom: 1px;
                  }}

                  h3 {{
                        margin-top: 30px;
                        color: #1d3557;
                        font-size: 22px;
                  }}

                  .contact {{
                        font-size: 16px;
                        color: #333;
                        margin-top:5px;
                        display: flex;
                        gap: 30px;
                        text-align:center;
                        justify-content:center;
                  }}

                  strong {{
                        color: #000;
                  }}

                  .resume-container p em {{
                        white-space: pre-wrap;
                        word-break: break-word;
                        max-width: 100%;
                        display: block;
                        overflow-wrap: anywhere;
                        max-height:4.6em;
                  }}
                  .resume-container p {{
                        white-space: pre-wrap;
                        word-break: break-word;
                        overflow-wrap: anywhere;
                        line-height: 1.4;
                        margin-top: 2px;
                        margin-bottom: 4px;
                  }}

                  .edu-row {{
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        margin-bottom: 4px;
                  }}

                  .college-name {{
                        font-weight: 600;
                        letter-spacing: 0.5px;
                        color: #1d3557;
                        font-size: 16px;
                        text-transform: uppercase;
                  }}

                  .passing-year {{
                        font-size: 14px;
                        color: #444;
                  }}

                  .course-title {{
                        margin-top: 2px;
                        font-style: italic;
                        color: #333;
                  }}
                  .button-row {{
                        display: flex;
                        justify-content: center;
                        gap: 20px;
                        margin-top: 30px;
                  }}

                  .btn {{
                        background-color: #e63946;
                        color: white;
                        padding: 10px 24px;
                        text-decoration: none;
                        border-radius: 6px;
                        font-weight: bold;
                        font-size: 16px;
                        transition: background 0.3s ease;
                  }}

                  .btn:hover {{
                        background-color: #d62828;
                  }}

                  .back-btn {{
                        background-color: #457b9d;
                  }}

                  .back-btn:hover {{
                        background-color: #1d3557;
                  }}
            </style>
      </head>
      <body>
            <div class="resume-container">
                  <h2>{(name).upper()}</h2>
                  <div class="contact">
                        <p>{email}</p>
                        <p>{phone}</p>
                  </div>
                  <hr>
                  {summary_html}
                  {education_html}
                  {skills_html}
                  {experience_html}
                  {project_html}
                  {certification_html}
            </div>
            <div class="button-row">
                  <a href="/" class="btn back-btn">Back</a>
                  <a href="/download_pdf" class="btn pdf-btn">Export PDF</a>
            </div>
      </body>
      </html>
      """
      with open("resume.html", "w", encoding="utf-8") as f:
            f.write(html)
      return HTMLResponse(content=html)



PDFSHIFT_API_KEY = "your secret api key"  # Get free key at https://pdfshift.io/

@app.get("/download_pdf")
async def download_pdf():
    # Read your HTML file
    with open("resume.html", "r", encoding="utf-8") as f:
        html_content = f.read()

    # Convert to PDF via API
    response = requests.post(
        "https://api.pdfshift.io/v3/convert/pdf",
        auth=("api", PDFSHIFT_API_KEY),
        json={"source": html_content},
        stream=True
    )

    # Save and return PDF
    with open("resume.pdf", "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)

    return FileResponse("resume.pdf", filename="resume.pdf")
