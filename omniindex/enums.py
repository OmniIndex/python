from enum import Enum
"""
Enumeration representing the different states of the OmniIndex system.

In this script, Enum is a class from the enum module, and OmniIndexState, OmniIndexAuthenticationType, ClientStatus, and LoginType are your custom enums. Each enum has several members, which are the possible states of the enum.

You can access the members of an enum like this:

```python
print(OmniIndexState.initialized)  # Output: OmniIndexState.initialized
print(OmniIndexState.initialized.value)  # Output: 2
```

"""
class OmniIndexState(Enum):
    """
    Represents the state of the OmniIndex system.
    """

    UNINITIALIZED = 1
    """
    Represents the state of the OmniIndex system when it has not been initialized yet.
    """

    INITIALIZED = 2
    """
    Represents the state of the OmniIndex system when it has been initialized.
    """

    INVALID = 3
    """
    Represents the state of the OmniIndex system when it is in an invalid state.
    """

    CONFIGURED = 4
    """
    Represents the state of the OmniIndex system when it has been configured.
    """

    AUTHORIZED = 5
    """
    Represents the state of the OmniIndex system when it has been authorized.
    """

    def __str__(self):
        """
        Returns a human-readable string representation of the Enum members.
        """
        return self.name

    def __repr__(self):
        """
        Returns a machine-readable string representation of the Enum members.
        """
        return f"OmniIndexState.{self.name}"

    def get_description(self):
        """
        Returns the description of the state.
        """
        if self == OmniIndexState.UNINITIALIZED:
            return "Represents the state of the OmniIndex system when it has not been initialized yet."
        elif self == OmniIndexState.INITIALIZED:
            return "Represents the state of the OmniIndex system when it has been initialized."
        elif self == OmniIndexState.INVALID:
            return "Represents the state of the OmniIndex system when it is in an invalid state."
        elif self == OmniIndexState.CONFIGURED:
            return "Represents the state of the OmniIndex system when it has been configured."
        elif self == OmniIndexState.AUTHORIZED:
            return "Represents the state of the OmniIndex system when it has been authorized."

class OmniIndexAuthenticationType(Enum):
    """
    Represents the authentication type for the OmniIndex service.

    Attributes:
        api (int): Represents the API authentication type.
        omniindex (int): Represents the OmniIndex authentication type.
    """
    api = 1
    omniindex = 2

class ClientStatus(Enum):
    """
    Represents the status of a client.

    Attributes:
        INVALID (int): Represents an invalid status.
        UNINITIALIZED (int): Represents an uninitialized status.
        INITIALIZED (int): Represents an initialized status.
        UNAUTHENTICATED (int): Represents an unauthenticated status.
        AUTHENTICATING (int): Represents an authenticating status.
        AUTHENTICATED (int): Represents an authenticated status.
    """
    INVALID = 1
    UNINITIALISED = 2
    INITIALIZED = 3
    UNAUTHENTICATED = 4
    AUTHENTICATING = 5
    AUTHENTICATED = 6

class LoginType(Enum):
    """
    Represents the type of login.

    Attributes:
        email (int): Represents an email login type.
        google (int): Represents a Google login type.
        apple (int): Represents an Apple login type.
        facebook (int): Represents a Facebook login type.
        register (int): Represents a registration login type.
        forgotPassword (int): Represents a forgot password login type.
        changeEmail (int): Represents a change email login type.
    """
    email = 1
    google = 2
    apple = 3
    facebook = 4
    register = 5
    forgotPassword = 6
    changeEmail = 7
