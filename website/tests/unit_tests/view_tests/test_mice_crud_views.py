"""
class AddMouseViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.login(username="testuser", password="testpassword")
        self.project = Project.objects.create(project_name="TestProject")

    # Access add_preexisting_mouse_to_project while logged in
    def test_add_preexisting_mouse_to_project_get(self):
        url = reverse(
            "add_preexisting_mouse_to_project", args=[self.project.project_name]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "researcher/add_preexisting_mouse_to_project.html"
        )
        self.assertIsInstance(response.context["mice_form"], ProjectMiceForm)
        self.assertEqual(response.context["project_name"], self.project.project_name)

    # Add valid data test here
    #Likely similar valid POST issue as edit_mouse test, below, where genotyper field causes issues

    def test_add_preexisting_mouse_to_project_post_invalid(self):
        url = reverse(
            "add_preexisting_mouse_to_project", args=[self.project.project_name]
        )
        data = {
            "sex": "Invalid",
            "dob": "2022-01-01",
            "genotyped": True,
            "project": self.project.project_name,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "researcher/add_preexisting_mouse_to_project.html"
        )
        self.assertIsInstance(response.context["mice_form"], ProjectMiceForm)
        self.assertEqual(response.context["project_name"], self.project.project_name)
        self.assertFalse(Mouse.objects.exists())

    # Access add_preexisting_mouse_to_project without logging in
    def test_add_preexisting_mouse_to_project_view_login_required(self):
        self.client.logout()
        url = reverse(
            "add_preexisting_mouse_to_project", args=[self.project.project_name]
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next={url}")


##################
### EDIT MOUSE ###
##################
class EditMouseViewTest(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.login(username="testuser", password="testpassword")
        self.project = Project.objects.create(project_name="TestProject")
        self.genotyper = CustomUser.objects.create_user(
            username="TestGenotyper",
            email="testgenotyper@example.com",
            password="testpassword",
        )
        self.mouse1 = Mouse.objects.create(
            sex="M", dob=date.today(), genotyped=True, project=self.project
        )
        self.mouse2 = Mouse.objects.create(
            sex="F", dob=date.today(), genotyped=True, project=self.project
        )
        self.mouse3 = Mouse.objects.create(
            sex="M", dob=date.today(), genotyped=True, project=self.project
        )

        self.strain = Strain.objects.create(strain_name="TestStrain")

    # Access edit_mouse while logged in
    def test_edit_mouse_get(self):
        url = reverse("edit_mouse", args=[self.project.project_name, self.mouse1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit_mouse.html")
        self.assertIsInstance(response.context["form"], ProjectMiceForm)
        self.assertEqual(response.context["form"].instance, self.mouse1)
        self.assertEqual(response.context["project_name"], self.project.project_name)

    # Can't get this valid POST test to work correctly. Genotyper field causes issues
    # POST with valid data
    def test_edit_mouse_post_valid(self):
        url = reverse('edit_mouse', args=[self.project.project_name, self.mouse1.id])
        data = {
            'sex': 'M',
            'dob': date.today(),
            'clipped_date': date.today(),
            'genotyped': True,
            'mother': self.mouse2,
            'father': self.mouse3,
            'cage': self.cage,
            'project': self.project,
            'genotyper': self.genotyper,
            'strain': self.strain,
            'earmark': 'BR',
        }
        response = self.client.post(url, data)
        form = response.context['form']
        print("form.errors")
        print(form.errors)
        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'show_project.html')

    # POST with invalid data
    def test_edit_mouse_post_invalid(self):
        url = reverse("edit_mouse", args=[self.project.project_name, self.mouse1.id])
        data = {
            "sex": "Invalid",
            "dob": date.today(),
            "genotyped": False,
            "project": self.project.project_name,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "edit_mouse.html")
        self.assertIsInstance(response.context["form"], ProjectMiceForm)
        self.assertEqual(response.context["project_name"], self.project.project_name)
        self.mouse1.refresh_from_db()
        self.assertEqual(self.mouse1.sex, "M")
        self.assertEqual(self.mouse1.dob, date.today())
        self.assertTrue(self.mouse1.genotyped)

    # Access edit_mouse without logging in
    def test_edit_mouse_view_with_unauthenticated_user(self):
        self.client.logout()
        url = reverse("edit_mouse", args=[self.project.project_name, self.mouse1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f"/accounts/login/?next={url}")
"""