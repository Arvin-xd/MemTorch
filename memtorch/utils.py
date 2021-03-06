import memtorch
import torch
import torchvision
from torchvision import datasets, transforms


def convert_range(old_value, old_min, old_max, new_min, new_max):
    """Method to convert values between two ranges.

    Parameters
    ----------
    old_value : object
        Old value(s) to convert. May be a single number, vector or tensor.
    old_min : float
        Minimum old value.
    old_max : float
        Maximum old value.
    new_min : float
        Minimum new value.
    new_max : float
        Maximum new value.

    Returns
    -------
    object
        New value(s).
    """
    return (((old_value - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min

def clip(value, lower, upper):
    """Method to clip a float between lower and upper bounds.

    Parameters
    ----------
    value : float
        Value to clip.
    lower : float
        Lower bound.
    upper : float
        Upper bound.

    Returns
    -------
    float
        Clipped float.
    """
    return lower if value < lower else upper if value > upper else value

def LoadMNIST(batch_size=32, validation=True):
    """Method to load the MNIST dataset.

    Parameters
    ----------
    batch_size : int
        Batch size.
    validation : bool
        Load the validation set (True).

    Returns
    -------
    list of torch.utils.data
        The train, validiation, and test loaders.
    """
    root = 'data'
    transform = transforms.Compose([transforms.ToTensor()])
    full_train_set = torchvision.datasets.MNIST(root=root, train=True, transform=transform, download=True)
    test_set = torchvision.datasets.MNIST(root=root, train=False, transform=transform, download=True)
    if validation:
        train_size = int(0.8 * len(full_train_set))
        validation_size = len(full_train_set) - train_size
        train_set, validation_set = torch.utils.data.random_split(full_train_set, [train_size, validation_size])
        train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=2)
        validation_loader = torch.utils.data.DataLoader(validation_set, batch_size=batch_size, shuffle=True, num_workers=2)
    else:
        train_loader = torch.utils.data.DataLoader(full_train_set, batch_size=batch_size, shuffle=True, num_workers=2)
        validation_loader = None

    test_loader = torch.utils.data.DataLoader(test_set, batch_size=int(batch_size/2), shuffle=False, num_workers=2)
    return train_loader, validation_loader, test_loader

def LoadCIFAR10(batch_size=32, validation=True):
    """Method to load the CIFAR-10 dataset.

    Parameters
    ----------
    batch_size : int
        Batch size.
    validation : bool
        Load the validation set (True).

    Returns
    -------
    list of torch.utils.data
        The train, validiation, and test loaders.
    """
    root = 'data'
    transform = transforms.Compose([transforms.ToTensor()])
    full_train_set = torchvision.datasets.CIFAR10(root=root, train=True, download=True, transform=transform)
    test_set = torchvision.datasets.CIFAR10(root=root, train=False, download=True, transform=transform)
    if validation:
        train_size = int(0.8 * len(full_train_set))
        validation_size = len(full_train_set) - train_size
        train_set, validation_set = torch.utils.data.random_split(full_train_set, [train_size, validation_size])
        train_loader = torch.utils.data.DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=2)
        validation_loader = torch.utils.data.DataLoader(validation_set, batch_size=batch_size, shuffle=True, num_workers=2)
    else:
        train_loader = torch.utils.data.DataLoader(full_train_set, batch_size=batch_size, shuffle=True, num_workers=2)
        validation_loader = None

    test_loader = torch.utils.data.DataLoader(test_set, batch_size=int(batch_size/2), shuffle=False, num_workers=2)
    return train_loader, validation_loader, test_loader
