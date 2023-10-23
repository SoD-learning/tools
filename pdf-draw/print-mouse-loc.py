import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Draw on PDF")

    # Create a canvas to potentially display your PDF and capture drawing input
    canvas = tk.Canvas(root, bg="white", width=600, height=600)
    canvas.pack()

    # Set up events for drawing (you'd need to add more logic for actual drawing)
    canvas.bind(
        "<Motion>", mouse_dragged
    )  # for example, you might draw while the mouse is dragged

    root.mainloop()


def mouse_dragged(event):
    # Here you would handle mouse movements for drawing
    print(f"Dragging at {event.x}, {event.y}")


if __name__ == "__main__":
    main()
