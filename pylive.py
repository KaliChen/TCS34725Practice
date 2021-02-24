import matplotlib.pyplot as plt
import numpy as np

# use ggplot style for more sophisticated visuals
plt.style.use('ggplot')

def live_plotter(x_vec,y1_data,line1,identifier='',pause_time=0.1):
    if line1==[]:
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
        # create a variable for the line so we can later update it
        line1, = ax.plot(x_vec,y1_data,'-o',alpha=0.8)        
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line1.set_ydata(y1_data)
    # adjust limits if new data goes beyond bounds
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])
    # this pauses the data so the figure/axis can catch up - the amount of pause can be altered above
    plt.pause(pause_time)
    
    # return line so we can update it again in the next iteration
    return line1
   
def live_plotter_Data_0_7(x_vec,
                          y0_data,
                          y1_data,
                          y2_data,
                          y3_data,
                          y4_data,
                          y5_data,
                          y6_data,
                          y7_data,
                          #current_time,
                          line0,line1,line2,line3,line4,line5,line6,line7,
                          identifier='',
                          pause_time=0.1):
    if(line0==[] or line1==[] or line2==[] or line3==[] or line4==[] or line5==[] or line6==[] or line7==[]):
        # this is the call to matplotlib that allows dynamic plotting
        plt.ion()
        fig = plt.figure(figsize=(15,7))

        ax = fig.add_subplot(111)
        bx = fig.add_subplot(111)
        cx = fig.add_subplot(111)
        dx = fig.add_subplot(111)
        ex = fig.add_subplot(111)
        fx = fig.add_subplot(111)
        gx = fig.add_subplot(111)
        hx = fig.add_subplot(111)
        
        # create a variable for the line so we can later update it
        line0, = ax.plot(x_vec,y0_data,'-o',alpha=0.8, color='red') 
        line1, = bx.plot(x_vec,y1_data,'-o',alpha=0.8, color='orange')        
        line2, = cx.plot(x_vec,y2_data,'-o',alpha=0.8, color='yellow')        
        line3, = dx.plot(x_vec,y3_data,'-o',alpha=0.8, color='green')        
        line4, = ex.plot(x_vec,y4_data,'-o',alpha=0.8, color='blue')        
        line5, = fx.plot(x_vec,y5_data,'-o',alpha=0.8, color='navy')        
        line6, = gx.plot(x_vec,y6_data,'-o',alpha=0.8, color='purple')        
        line7, = hx.plot(x_vec,y7_data,'-o',alpha=0.8, color='gray')        
        
        #update plot label/title
        plt.ylabel('Y Label')
        plt.title('Title: {}'.format(identifier))
        plt.show()
    
    # after the figure, axis, and line are created, we only need to update the y-data
    line0.set_ydata(y0_data)
    line1.set_ydata(y1_data)
    line2.set_ydata(y2_data)
    line3.set_ydata(y3_data)
    line4.set_ydata(y4_data)
    line5.set_ydata(y5_data)
    line6.set_ydata(y6_data)
    line7.set_ydata(y7_data)
    plt.pause(pause_time)
    
    
    # return line so we can update it again in the next iteration
    return (line0,line1,line2,line3,line4,line5,line6,line7)
