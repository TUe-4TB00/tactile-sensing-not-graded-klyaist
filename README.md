# Installation

This is an ungraded programming assignment. The solutions can be found in `answers.py`. There are no tests.

Some basic dependencies are needed for running the code. We use a virtual environment as before. If you like you can reuse the virtual environment created for the reinforcement learning assignment.

## Creating and using a virtual environment
Create a virtual environment:

```bash
python -m venv myenv
```

Now you have created a virtual environment, but it is not active yet. To activate this environment, type the appropriate command:

* Windows:
```bash
myenv\Scripts\activate
```

* Mac/Linux:
```bash
source myenv/bin/activate
```

Once you have activated a virtual environment, the *only* packages installed within this environment will be used. Installing new and removing existing packages will *only* happen within your environment. To make sure all required dependencies are installed within this virtual environment, install all dependencies that we have defined (**make sure your virtual environment is active when running this command**):

```bash
pip install -r requirements.txt
```

