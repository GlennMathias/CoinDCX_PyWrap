class Analytics:
    def __init__(self):
        pass

    def RSI(self,data,n):
        #100 -(100/(1+(Avg Gain/Avg Loss)))
        gains=[]
        losses=[]
        size=len(data)

        rsis=[]
        #alpha=2/(n+1)
        alpha=1/n

        for i in range(0,size-n):
            for j in range(i+1,i+n):
                if data[j]>data[j-1]:
                    gains.append(data[j]-data[j-1])
                    losses.append(0)
                elif data[j]==data[j-1]:
                    losses.append(0)
                    gains.append(0)
                else:
                    losses.append(data[j-1]-data[j])
                    gains.append(0)
                    
            total_gains=sum(gains[:-1])
            total_loss=sum(losses[:-1])
            
            if total_gains == 0:
                avg_gains=1;
            else:
                avg_gain=total_gains/(len(gains)-1)

            if total_loss == 0:
                avg_loss=0.001;
            else:
                avg_loss=total_loss/(len(losses)-1)

            avg_gain=gains[-1]*alpha+avg_gain*(1-alpha)
            avg_loss=losses[-1]*alpha+avg_loss*(1-alpha)

            print(avg_gain,avg_loss,avg_gain/avg_loss)
                    
            rsi=100 -(100/ (1+ (avg_gain/avg_loss) ) )
            rsis.append(rsi)
        
        return rsis

    def MA(self,data,n):
        ma=[]
        for i in range(0,len(data)-n):
            ma.append( sum(data[i:i+n])/n )

        return ma
