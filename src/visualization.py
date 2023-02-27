from matplotlib.pyplot import figure, show

def three_dimensional_plotting(arrOfPoint:list, pointA:list, pointB:list, name:str = "") :
    fig = figure(num=name)

    # 3D plot from array of points
    ax = fig.add_subplot(111, projection='3d')
    for point in arrOfPoint:
        ax.scatter(point[0], point[1], point[2], color='blue')
    
    ax.scatter(pointA[0], pointA[1], pointA[2], color='red')
    ax.scatter(pointB[0], pointB[1], pointB[2], color='red')
    show()
