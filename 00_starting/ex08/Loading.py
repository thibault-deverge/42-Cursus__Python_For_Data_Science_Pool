
def ft_tqdm(lst: range) -> None:
    """
    Custom tqdm function to display a progress bar
    """
    range_len = len(lst)
    bar_len = 150

    if range_len == 0:
        print("0it")
        return

    for index, element in enumerate(lst, start=1):
        # Calculate progress (from 0 to 1) and progress of the bar
        progress = index / range_len
        bar_progress = int(bar_len * progress)
        bar_remaining = bar_len - bar_progress

        # Save the differents parts of the message to display
        percentage = int(progress * 100)
        bar = f"|{'█' * bar_progress}{' ' * bar_remaining}|"
        fraction = f" {index}/{len(lst)} "

        # Print message
        message = f"\r{percentage}%{bar}{fraction}"
        print(message, end='', flush=True)

        yield element
