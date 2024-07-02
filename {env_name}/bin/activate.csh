# This file must be used with "source bin/activate.csh" *from csh/tcsh*
# you cannot run it directly

# Function to deactivate the virtual environment
deactivate () {
    # Reset old environment variables
    if ( $?_OLD_VIRTUAL_PATH ) then
        setenv PATH $_OLD_VIRTUAL_PATH
        unsetenv _OLD_VIRTUAL_PATH
    endif
    if ( $?_OLD_VIRTUAL_PYTHONHOME ) then
        setenv PYTHONHOME $_OLD_VIRTUAL_PYTHONHOME
        unsetenv _OLD_VIRTUAL_PYTHONHOME
    endif

    unsetenv VIRTUAL_ENV
    if ( "$1" != "nondestructive" ) then
        # Self-destruct!
        unset deactivate
    endif
}

# Unset irrelevant variables before activating new environment
deactivate nondestructive

# Set the virtual environment path
setenv VIRTUAL_ENV "/Users/estudio/Projects/GitHub/Python/catalina-politician-insight-sql/catalina-politician-insight-sql/{env_name}"

# Save the current PATH and update it to include the virtual environment bin directory
setenv _OLD_VIRTUAL_PATH "$PATH"
setenv PATH "$VIRTUAL_ENV/bin:$PATH"

# Unset PYTHONHOME if it is set
if ( $?PYTHONHOME ) then
    setenv _OLD_VIRTUAL_PYTHONHOME "$PYTHONHOME"
    unsetenv PYTHONHOME
endif

# If the prompt is not disabled, override the shell prompt to include the virtual environment name
if ( ! $?VIRTUAL_ENV_DISABLE_PROMPT ) then
    alias precmd 'set prompt = "(${env_name}) $prompt"'
endif
