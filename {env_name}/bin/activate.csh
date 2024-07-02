# This file must be used with "source bin/activate.csh" *from csh/tcsh*
# you cannot run it directly

# Function to deactivate the virtual environment
deactivate () {
    ...
}

# Check if virtual environment is already active
if ( $?VIRTUAL_ENV ) then
    echo "Virtual environment already active"
else
    # Activate the virtual environment
    setenv VIRTUAL_ENV /path/to/virtualenv
    setenv PATH ${VIRTUAL_ENV}/bin:${PATH}
    echo "Virtual environment activated"
endif
