from django import forms
from django.core.validators import RegexValidator
from Resources.models import Department, Course, Branch, Semester, Student, Faculty

CATEGORY_CHOICES = (("General", "General"), ("OBC", "OBC"), ("SC", "SC"), ("ST", "ST"),)
POST_CHOICES = (("Professor", "Professor"), ("Assistant Professor", "Assistant Professor"), ("Lab Technician", "Lab Technician"), ("Associate Professor", "Associate Professor"),)

indian_number_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="Enter a 10-digit phone number."
)

username_validator = RegexValidator(
    regex=r'^[a-zA-Z]*$',
    message="Name must contain only characters.",
)

class AdminLoginForm(forms.Form):
    # Admin Login Form
    Username = forms.CharField(required=True, max_length=150, error_messages={'required': 'Please write your username'}, widget=forms.TextInput({'class': 'form-control form-control-user', 'placeholder': 'Username'}))
    Password = forms.CharField(required=True, max_length=64, error_messages={'required': 'Please write your password'}, widget=forms.PasswordInput({'class': 'form-control form-control-user', 'placeholder': 'Password'}))

class StudentFacultyLoginForm(forms.Form):
    # Student and Faculty Login Form
    Email = forms.EmailField(required=True, error_messages={'required': 'Please write your email'}, widget=forms.EmailInput({'class': 'form-control form-control-user', 'placeholder': 'Email'}))
    Password = forms.CharField(required=True, max_length=64, error_messages={'required': 'Please write your password'}, widget=forms.PasswordInput({'class': 'form-control form-control-user', 'placeholder': 'Password'}))
    UserType = forms.ChoiceField(required=True, choices=[('student', 'Student'), ('faculty', 'Faculty')], widget=forms.Select({'class': 'form-control'}))

class RegistrationForm(forms.Form):
    # Registration Form
    UserType = forms.ChoiceField(required=True, choices=[('student', 'Student'), ('faculty', 'Faculty')], widget=forms.Select({'class': 'form-control', 'onchange': 'typeSelect();'}))
    Email = forms.EmailField(required=True, error_messages={'required': 'Please write your email'}, widget=forms.EmailInput({'class': 'form-control form-control-user', 'placeholder': 'Email'}))
    FirstName = forms.CharField(required=True, max_length=150, error_messages={'required': 'Please write your first name'}, widget=forms.TextInput({'class': 'form-control form-control-user', 'placeholder': 'First Name'}))
    LastName = forms.CharField(required=True, max_length=150, error_messages={'required': 'Please write your last name'}, widget=forms.TextInput({'class': 'form-control form-control-user', 'placeholder': 'Last Name'}))
    Password = forms.CharField(required=True, max_length=64, error_messages={'required': 'Please write your password'}, widget=forms.PasswordInput({'class': 'form-control form-control-user', 'placeholder': 'Password'}))
    ConfirmPassword = forms.CharField(required=True, max_length=64, error_messages={'required': 'Please confirm your password'}, widget=forms.PasswordInput({'class': 'form-control form-control-user', 'placeholder': 'Confirm Password'}))
    Enrollment = forms.CharField(required=False, label="Enrollment Number", max_length=64, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Enrollment', 'onBlur': "CheckEnroll();"}))
    EmployeeID = forms.CharField(required=False, label="Employee ID", max_length=64, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Employee ID', 'onBlur': "CheckEmployee();"}))
    Contact = forms.CharField(
        required=True, 
        label="Contact (10 Digits)", 
        max_length=10,
        # Temporarily disable the validator for testing
        # validators=[indian_number_validator],
        widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Phone Number'})
    )
    Category = forms.ChoiceField(required=False, label="Category", choices=CATEGORY_CHOICES, widget=forms.Select({'class': 'form-control'}))
    Post = forms.ChoiceField(required=False, label="Post", choices=POST_CHOICES, widget=forms.Select({'class': 'form-control'}))
    Qualification = forms.CharField(required=False, label="Qualifications", max_length=1024, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Qualifications'}))
    Joining = forms.DateField(required=False, label="Date of Joining", widget=forms.DateInput({'class': 'form-control', 'type': 'date', 'min': '1950-01-01', 'max': '2021-12-31'}))
    Photo = forms.FileField(required=True, label="Photo (jpg - 2 MB)", widget=forms.FileInput({'class': 'form-control', 'accept': 'image/jpg'}))
    DOB = forms.DateField(required=True, label="Date of Birth", widget=forms.DateInput({'class': 'form-control', 'type': 'date', 'min': '1950-01-01', 'max': '2010-12-31'}))
    Address = forms.CharField(required=True, label="Address", max_length=1024, widget=forms.TextInput({'class': 'form-control', 'placeholder': 'Full Address'}))
    Department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,  # Make it not required initially
        label="Department",
        widget=forms.Select({'class': 'form-control', 'onchange': 'onDepartmentChange();'})
    )
    Course = forms.ModelChoiceField(
        queryset=Course.objects.all(),  # Use all courses initially
        required=False,
        label="Course",
        widget=forms.Select({'class': 'form-control', 'onchange': 'onCourseChange();'})
    )
    Branch = forms.ModelChoiceField(
        queryset=Branch.objects.all(),  # Use all branches initially
        required=False,
        label="Branch",
        widget=forms.Select({'class': 'form-control', 'onchange': 'onBranchChange();'})
    )
    Semester = forms.ModelChoiceField(
        queryset=Semester.objects.all(),  # Use all semesters initially
        required=False,
        label="Semester",
        widget=forms.Select({'class': 'form-control'})
    )

    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        if Student.objects.filter(Email=email).exists() or Faculty.objects.filter(Email=email).exists():
            raise forms.ValidationError("Email already exists.")
        return email

    def clean_Enrollment(self):
        enrollment = self.cleaned_data.get('Enrollment')
        if enrollment and Student.objects.filter(Enrollment=enrollment).exists():
            raise forms.ValidationError("Enrollment number already exists.")
        return enrollment

    def clean_EmployeeID(self):
        employee_id = self.cleaned_data.get('EmployeeID')
        if employee_id and Faculty.objects.filter(FacultyCollegeID=employee_id).exists():
            raise forms.ValidationError("Employee ID already exists.")
        return employee_id

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('UserType')
        
        # Only validate student-specific fields if user type is student
        if user_type == 'student':
            # Check that required fields for students are filled in
            required_fields = ['Enrollment', 'Category', 'Department', 'Course', 'Branch', 'Semester']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f'{field} is required for students')
        
        # Only validate faculty-specific fields if user type is faculty
        elif user_type == 'faculty':
            # Check that required fields for faculty are filled in
            required_fields = ['EmployeeID', 'Post', 'Qualification', 'Joining']
            for field in required_fields:
                if not cleaned_data.get(field):
                    self.add_error(field, f'{field} is required for faculty')
        
        return cleaned_data
