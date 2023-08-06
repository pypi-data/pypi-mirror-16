CCH - Cloud CLI for Humans.

Very simple cloud CLI, specifically designed for human interaction.

Just type `mkvm` and it will help you step-by-step create a virtual machine, by
first providing a flavor, then a security group, and then root volume storage.
All the other commands are just as simple!

All commands:

    lsvm    - List all virtual machines
    mkvm    - Create a virtual machine
    stpvm   - Stop a virtual machine
    rmvm    - Terminate a virtual machine

    lskp    - List all keypairs
    mkkp    - Create keypairs
    rmkp    - Delete a keypair

    lssg    - List all security groups (including a detailed view)
    mksg    - Create a security group (including specifying secgroup rules)
    rmsg    - Delete a security group


## Installation

    pip install cch



