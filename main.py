from fastapi import FastAPI ,Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import requests
from fastapi.responses import FileResponse

app = FastAPI()
# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=HTMLResponse)
def homepage():
      html = """
      <html>
      <head>
            <title>Homepage</title>
            <style>
                  body { 
                        font-family: Arial, sans-serif; 
                        margin: 0; 
                        padding: 0; 
                        background: #f8fafc;
                  }
                  header { 
                        background: #1f2937; 
                        color: white; 
                        padding: 20px 40px; 
                        display: flex; 
                        justify-content: space-between; 
                        align-items: center; 
                        box-shadow: 0 2px 8px rgba(31,41,55,0.07);
                  }
                  .logo {
                        font-size: 2rem;
                        font-weight: bold;
                        letter-spacing: 1px;
                  }
                  nav ul { 
                        list-style: none; 
                        display: flex; 
                        gap: 28px; 
                        margin: 0; 
                        padding: 0; 
                  }
                  nav ul li a { 
                        color: white; 
                        text-decoration: none; 
                        font-weight: 500; 
                        font-size: 1.1rem;
                        transition: color 0.2s;
                  }
                  nav ul li a:hover {
                        color: #a5b4fc;
                  }
                  .hero { 
                        text-align: center; 
                        padding: 10% 20px 30% ; 
                        background: linear-gradient(120deg, #f3f4f6 0%, #e0e7ff 100%);
                  }
                  .hero h1 { 
                        font-size: 2.5rem; 
                        margin-bottom: 16px; 
                        color: #1f2937;
                        font-weight: 700;
                  }
                  .hero p { 
                        font-size: 1.25rem; 
                        margin-bottom: 32px; 
                        color: #374151;
                  }
                  .btn { 
                        padding: 0.6em 2em;
                        border: none;
                        outline: none;
                        color: rgb(255, 255, 255);
                        background: #111;
                        cursor: pointer;
                        position: relative;
                        z-index: 0;
                        border-radius: 10px;
                        user-select: none;
                        -webkit-user-select: none;
                        touch-action: manipulation;
                  }
                  .btn:before {
                        content: "";
                        background: linear-gradient(
                              45deg,
                              #ff0000,
                              #ff7300,
                              #fffb00,
                              #48ff00,
                              #00ffd5,
                              #002bff,
                              #7a00ff,
                              #ff00c8,
                              #ff0000
                        );
                        position: absolute;
                        top: -2px;
                        left: -2px;
                        background-size: 400%;
                        z-index: -1;
                        filter: blur(5px);
                        -webkit-filter: blur(5px);
                        width: calc(100% + 4px);
                        height: calc(100% + 4px);
                        animation: glowing-btn 20s linear infinite;
                        transition: opacity 0.3s ease-in-out;
                        border-radius: 10px;
                  }
                  @keyframes glowing-btn {
                        0% {
                              background-position: 0 0;
                        }
                        50% {
                              background-position: 400% 0;
                        }
                        100% {
                              background-position: 0 0;
                        }
                  }
                  .btn:after {
                        z-index: -1;
                        content: "";
                        position: absolute;
                        width: 100%;
                        height: 100%;
                        background: #222;
                        left: 0;
                        top: 0;
                        border-radius: 10px;
                  }
                  .footer{
                        background:#0f172a; 
                        color:#94a3b8; 
                        text-align:center;
                        padding:20px;
                        font-family:Arial;
                  }
                  .arrow{
                        text-align:center;
                        max-height:18px;
                        width:18px;
                        display:inline-block;
                        margin:20px 0;
                        object-fit:content;
                  }
            </style>
      </head>
      <body>
            <header>
                  <div class="logo">Resume Builder</div>
                  <nav>
                        <ul>
                              <li><a href="#">Menu</a></li>
                              <li><a href="#">Contact Us</a></li>
                        </ul>
                  </nav>
            </header>
            <section class="hero">
                  <h1>The Best And Easy Online Resume Builder</h1>
                  <p>Easily create a resume for any job using our best-in-class platform.</p>
                  <br><br><br><br>
                  <a href="/form" class="btn">Create Resume Now</a>
            </section>
            <div class="footer">
                  <footer>
                        © 2025 ResumeBuilder. All rights reserved.
                  </footer>
            </div>
      </body>
      </html>
      """
      return HTMLResponse(content=html)

@app.get("/form" ,response_class=HTMLResponse)
def resume_form():
      html="""
      <html>
            <head>
                  <title>Resume Form</title>
                  <style>
                        body {
                        background: linear-gradient(120deg, #f3f4f6 0%, #e0e7ff 100%);
                        font-family: 'Segoe UI', Arial, sans-serif;
                        margin: 0;
                        padding: 0;
                        min-height: 100vh;
                  }
                  .header {
                        width: 100%;
                        background: #1f2937;
                        color: #fff;
                        padding: 24px 0 16px 0;
                        text-align: center;
                        font-size: 2rem;
                        font-weight: bold;
                        letter-spacing: 1px;
                        box-shadow: 0 2px 8px rgba(31,41,55,0.07);
                  }
                  .footer {
                        width: 100%;
                        background: #0f172a;
                        color: #94a3b8;
                        text-align: center;
                        padding: 18px 0 10px 0;
                        font-size: 1rem;
                        letter-spacing: 0.5px;
                        box-shadow: 0 -2px 8px rgba(31,41,55,0.07);
                        margin-top: 40px;
                  }
                  .form-container {
                        max-width: 600px;
                        margin: 40px auto 80px auto;
                        background: #fff;
                        border-radius: 16px;
                        box-shadow: 0 8px 32px rgba(60, 72, 88, 0.15);
                        padding: 40px 36px 32px 36px;
                        position: relative;
                  }
                  h1 {
                        text-align: center;
                        color: #1f2937;
                        margin-bottom: 28px;
                        font-size: 2.2rem;
                        letter-spacing: 1px;
                        font-weight: 700;
                  }
                  h4, h5 {
                        color: #4f46e5;
                        margin-bottom: 8px;
                        margin-top: 24px;
                        font-weight: 600;
                  }
                  h5 {
                        font-size: 1.1rem;
                        color: #6366f1;
                        margin-top: 16px;
                  }
                  input[type="text"], input[type="email"], input[type="tel"], input[type="int"], textarea {
                        width: 100%;
                        padding: 12px 16px;
                        margin: 6px 0 14px 0;
                        border: 1.5px solid #a5b4fc;
                        border-radius: 8px;
                        font-size: 1rem;
                        background: #f1f5f9;
                        transition: border 0.2s, box-shadow 0.2s;
                        box-sizing: border-box;
                        color: #1e293b;
                  }
                  input[type="text"]:focus, input[type="email"]:focus, input[type="tel"]:focus, input[type="int"]:focus, textarea:focus {
                        border: 1.5px solid #6366f1;
                        outline: none;
                        background: #fff;
                        box-shadow: 0 0 0 2px #a5b4fc33;
                  }
                  textarea {
                        min-height: 60px;
                        resize: vertical;
                  }
                  .button-center {
                        
                        margin-top: 18px;
                  }
                  button[type="submit"] {
                        width: 50%;
                        background: linear-gradient(90deg, #6366f1 0%, #4f46e5 100%);
                        color: #fff;
                        border: none;
                        border-radius: 8px;
                        padding: 14px 0;
                        font-size: 1.1rem;
                        font-weight: 600;
                        letter-spacing: 0.5px;
                        cursor: pointer;
                        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.08);
                        transition: background 0.2s, transform 0.1s;
                        text-align:center;
                        display: block;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                  }
                  button[type="submit"]:hover {
                        background: linear-gradient(90deg, #4f46e5 0%, #6366f1 100%);
                        transform: translateY(-2px) scale(1.01);
                  }
                  ::placeholder {
                        color: #a5b4fc;
                        opacity: 1;
                  }
                  @media (max-width: 700px) {
                        .form-container {
                              padding: 24px 8vw 18px 8vw;
                        }
                        .header, .footer {
                              font-size: 1.2rem;
                        }
                        button[type="submit"] {
                              width: 100%;
                        }
                  }
                  .resume-box {
                        margin-top: 0;
                  }
                  label {
                        font-weight: 500;
                        color: #374151;
                        margin-bottom: 4px;
                        display: block;
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
                        <div class="footer">
                        &copy; 2025 Resume Builder. All rights reserved.
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
