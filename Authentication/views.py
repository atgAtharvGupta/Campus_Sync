from django.shortcuts import render, redirect
from .forms import AdminLoginForm, StudentFacultyLoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import permission_required, login_required
from Resources.models import Department, Course, Branch, Semester, Student, Faculty
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password

def loginAuth(request):
    if request.user.is_authenticated:
        return redirect(reverse('Administration:Dashboard'))

    admin_form = AdminLoginForm()
    student_faculty_form = StudentFacultyLoginForm()

    if request.method == 'POST':
        # Check if the admin login button was clicked
        if 'admin_login' in request.POST:
            admin_form = AdminLoginForm(request.POST)
            if admin_form.is_valid():
                username = admin_form.cleaned_data['Username']
                password = admin_form.cleaned_data['Password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect(reverse('Administration:Dashboard'))  # Admin dashboard
                else:
                    return render(request, 'Authentication/Login.html', {
                        'AdminForm': admin_form,
                        'StudentFacultyForm': student_faculty_form,
                        'Message': 'Wrong credentials, try again.',
                        'Visiblity': 'visible'
                    })
            else:
                return render(request, 'Authentication/Login.html', {
                    'AdminForm': admin_form,
                    'StudentFacultyForm': student_faculty_form,
                    'Message': 'Invalid form submission.',
                    'Visiblity': 'visible'
                })

        # Check if the student/faculty login button was clicked
        elif 'student_faculty_login' in request.POST:
            student_faculty_form = StudentFacultyLoginForm(request.POST)
            if student_faculty_form.is_valid():
                email = student_faculty_form.cleaned_data['Email']
                password = student_faculty_form.cleaned_data['Password']
                user_type = student_faculty_form.cleaned_data['UserType']
                print(f"Login attempt: {email}, {user_type}")
                if user_type == 'student':
                    try:
                        student = Student.objects.get(Email=email)
                        print(f"Found student: {student.First} {student.Last}")
                        if check_password(password, student.Password) or student.Password == password:
                            print("Password check successful")
                            # If it was a plain text match, hash it for future security
                            if student.Password == password:
                                student.Password = make_password(password)
                                student.save()
                                print("Password hashed for future use")
                            
                            # Check if user exists in Django auth system
                            try:
                                user = User.objects.get(username=email)
                            except User.DoesNotExist:
                                # Create Django user if doesn't exist
                                user = User.objects.create_user(
                                    username=email,
                                    email=email,
                                    password=password
                                )
                                user.first_name = student.First
                                user.last_name = student.Last
                                user.save()
                                print(f"Created Django user for {email}")
                            
                            # Log in the user using Django's auth system
                            login(request, user)
                            print(f"User {email} logged in successfully")
                            return redirect(reverse('Administration:Dashboard'))  # Use Administration dashboard
                        else:
                            print("Password check failed")
                            print(f"Input password: {password}")
                            print(f"Stored password: {student.Password}")
                            return render(request, 'Authentication/Login.html', {
                                'AdminForm': admin_form,
                                'StudentFacultyForm': student_faculty_form,
                                'Message': 'Wrong credentials, try again.',
                                'Visiblity': 'visible'
                            })
                    except Student.DoesNotExist:
                        return render(request, 'Authentication/Login.html', {
                            'AdminForm': admin_form,
                            'StudentFacultyForm': student_faculty_form,
                            'Message': 'Email does not exist.',
                            'Visiblity': 'visible'
                        })

                elif user_type == 'faculty':
                    try:
                        faculty = Faculty.objects.get(Email=email)
                        if check_password(password, faculty.Password) or faculty.Password == password:
                            print("Password check successful")
                            # If it was a plain text match, hash it for future security
                            if faculty.Password == password:
                                faculty.Password = make_password(password)
                                faculty.save()
                                print("Password hashed for future use")
                                
                            # Check if user exists in Django auth system
                            try:
                                user = User.objects.get(username=email)
                            except User.DoesNotExist:
                                # Create Django user if doesn't exist
                                user = User.objects.create_user(
                                    username=email,
                                    email=email,
                                    password=password
                                )
                                user.first_name = faculty.First
                                user.last_name = faculty.Last
                                user.save()
                                print(f"Created Django user for {email}")
                            
                            # Log in the user using Django's auth system
                            login(request, user)
                            print(f"User {email} logged in successfully")
                            return redirect(reverse('Administration:Dashboard'))  # Use Administration dashboard
                        else:
                            print("Password check failed")
                            print(f"Input password: {password}")
                            print(f"Stored password: {faculty.Password}")
                            return render(request, 'Authentication/Login.html', {
                                'AdminForm': admin_form,
                                'StudentFacultyForm': student_faculty_form,
                                'Message': 'Wrong credentials, try again.',
                                'Visiblity': 'visible'
                            })
                    except Faculty.DoesNotExist:
                        return render(request, 'Authentication/Login.html', {
                            'AdminForm': admin_form,
                            'StudentFacultyForm': student_faculty_form,
                            'Message': 'Email does not exist.',
                            'Visiblity': 'visible'
                        })
            else:
                return render(request, 'Authentication/Login.html', {
                    'AdminForm': admin_form,
                    'StudentFacultyForm': student_faculty_form,
                    'Message': 'Invalid form submission.',
                    'Visiblity': 'visible'
                })

    return render(request, 'Authentication/Login.html', {
        'AdminForm': admin_form,
        'StudentFacultyForm': student_faculty_form,
        'Message': '',
        'Visiblity': 'invisible'
    })

def registerAuth(request):
    if request.method == 'POST':
        # Print the full POST data for debugging
        print("POST data:", request.POST)
        print("FILES data:", request.FILES)
        
        form = RegistrationForm(request.POST, request.FILES)
        print("Form submitted, checking validity...")
        if form.is_valid():
            print("Form is valid")
            try:
                user_type = form.cleaned_data['UserType']
                email = form.cleaned_data['Email']
                first_name = form.cleaned_data['FirstName']
                last_name = form.cleaned_data['LastName']
                password = form.cleaned_data['Password']
                confirm_password = form.cleaned_data['ConfirmPassword']
                print(f"Processing registration for {user_type}: {email}")
                
                if password == confirm_password:
                    if User.objects.filter(username=email).count() == 0:
                        user = User.objects.create_user(email, email, password)
                        user.first_name = first_name
                        user.last_name = last_name
                        user.save()
                        print(f"Django user created: {email}")
                        
                        if user_type == 'student':
                            # Create student with correct field names
                            try:
                                # Get the model instances
                                department = form.cleaned_data['Department']
                                course = form.cleaned_data['Course']
                                branch = form.cleaned_data['Branch']
                                semester = form.cleaned_data['Semester']
                                
                                # Create student with correct field names
                                student = Student(
                                    First=first_name,
                                    Last=last_name,
                                    Email=email,
                                    Enrollment=form.cleaned_data['Enrollment'],
                                    Contact=form.cleaned_data['Contact'],
                                    Address=form.cleaned_data['Address'],
                                    DOB=form.cleaned_data['DOB'],
                                    Category=form.cleaned_data['Category'],
                                    Department_id=department,  # Note the _id suffix
                                    Course_id=course,          # Note the _id suffix
                                    Branch_id=branch,          # Note the _id suffix
                                    Semester_id=semester,      # Note the _id suffix
                                    Password=make_password(password)
                                )
                                
                                # Handle photo upload
                                if 'Photo' in request.FILES:
                                    import base64
                                    import io
                                    
                                    # Read the uploaded image
                                    photo_file = request.FILES['Photo']
                                    photo_data = photo_file.read()
                                    
                                    # Convert to base64 (as the Photo field is a TextField)
                                    encoded_photo = base64.b64encode(photo_data).decode('utf-8')
                                    student.Photo = encoded_photo
                                
                                student.save()
                                print("Student saved successfully")
                                
                                # Show success message and redirect
                                success_message = 'Registration successful!'
                                print(success_message)
                                return render(request, 'Authentication/Register.html', {
                                    'Form': RegistrationForm(),  # Fresh form
                                    'Message': success_message,
                                    'Visiblity': 'visible',
                                    'ShowAlert': True,
                                    'AlertMessage': success_message
                                })
                            except Exception as e:
                                print(f"Error saving student: {e}")
                                import traceback
                                traceback.print_exc()
                                return render(request, 'Authentication/Register.html', {
                                    'Form': form,
                                    'Message': f'Error saving student: {e}',
                                    'Visiblity': 'visible'
                                })
                                
                        elif user_type == 'faculty':
                            # Create faculty
                            try:
                                faculty = Faculty(
                                    First=first_name,
                                    Last=last_name,
                                    Email=email,
                                    Post=form.cleaned_data['Post'],
                                    Qualification=form.cleaned_data['Qualification'],
                                    FacultyCollegeID=form.cleaned_data['EmployeeID'],
                                    Contact=form.cleaned_data['Contact'],
                                    Address=form.cleaned_data['Address'],
                                    DOB=form.cleaned_data['DOB'],
                                    JoiningDate=form.cleaned_data['Joining'],
                                    Password=make_password(password)
                                )
                                
                                # Handle photo upload
                                if 'Photo' in request.FILES:
                                    import base64
                                    
                                    # Read the uploaded image
                                    photo_file = request.FILES['Photo']
                                    photo_data = photo_file.read()
                                    
                                    # Convert to base64 (as the Photo field is a TextField)
                                    encoded_photo = base64.b64encode(photo_data).decode('utf-8')
                                    faculty.Photo = encoded_photo
                                
                                faculty.save()
                                print("Faculty saved successfully")
                                
                                # Show success message and redirect
                                success_message = 'Registration successful!'
                                print(success_message)
                                return render(request, 'Authentication/Register.html', {
                                    'Form': RegistrationForm(),  # Fresh form
                                    'Message': success_message,
                                    'Visiblity': 'visible',
                                    'ShowAlert': True,
                                    'AlertMessage': success_message
                                })
                            except Exception as e:
                                print(f"Error saving faculty: {e}")
                                import traceback
                                traceback.print_exc()
                                return render(request, 'Authentication/Register.html', {
                                    'Form': form,
                                    'Message': f'Error saving faculty: {e}',
                                    'Visiblity': 'visible'
                                })
                    else:
                        return render(request, 'Authentication/Register.html', {
                            'Form': form,
                            'Message': 'Email already exists.',
                            'Visiblity': 'visible'
                        })
                else:
                    return render(request, 'Authentication/Register.html', {
                        'Form': form,
                        'Message': 'Passwords do not match.',
                        'Visiblity': 'visible'
                    })
            except Exception as e:
                print(f"Registration error: {e}")
                import traceback
                traceback.print_exc()
                return render(request, 'Authentication/Register.html', {
                    'Form': form,
                    'Message': f'Error during registration: {e}',
                    'Visiblity': 'visible'
                })
        else:
            print("Form is invalid")
            # Print specific field errors for debugging
            for field, errors in form.errors.items():
                print(f"Field {field} errors: {errors}")
            return render(request, 'Authentication/Register.html', {
                'Form': form,
                'Message': f'Invalid form submission. Please check all fields.',
                'Visiblity': 'visible'
            })
    else:
        form = RegistrationForm()
    return render(request, 'Authentication/Register.html', {
        'Form': form,
        'Message': '',
        'Visiblity': 'invisible'
    })

def logoutAuth(request):
    logout(request)
    return redirect(reverse('Authentication:Login'))

def get_course(request):
    department_id = request.POST.get('depart')
    print(f"Getting courses for department ID: {department_id}")
    courses = Course.objects.filter(Department_id=department_id).values_list('id', 'Name')
    courses_dict = {str(id): name for id, name in courses}
    print(f"Found courses: {courses_dict}")
    return JsonResponse(courses_dict)

def get_branch(request):
    course_id = request.POST.get('course')
    print(f"Getting branches for course ID: {course_id}")
    branches = Branch.objects.filter(Course_id=course_id).values_list('id', 'Name')
    branches_dict = {str(id): name for id, name in branches}
    print(f"Found branches: {branches_dict}")
    return JsonResponse(branches_dict)

def get_semester(request):
    branch_id = request.POST.get('branch')
    print(f"Getting semesters for branch ID: {branch_id}")
    semesters = Semester.objects.filter(Branch_id=branch_id).values_list('id', 'Name')
    semesters_dict = {str(id): name for id, name in semesters}
    print(f"Found semesters: {semesters_dict}")
    return JsonResponse(semesters_dict)

