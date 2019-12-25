
print(" ")
print("Printing results...")

print("###########################################################################")
print(" ")
print("K Means ALgorithm ...")
import KMeans_FINAL
print(" ")
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%kcpi_1," ","%.4f"%kintra_1," ","%.4f"%kinter_1," ","%.4f"%ksi_1," ","%.4f"%kmse_1," ","%.4f"%(kdi_1*10))
print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%kcpi_2," ","%.4f"%kintra_2," ","%.4f"%kinter_2," ","%.4f"%ksi_2," ","%.4f"%kmse_2," ","%.4f"%(kdi_2*10))
print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%kcpi_3," ","%.4f"%kintra_3,"  ","%.4f"%kinter_3,"  ","%.4f"%ksi_3,"  ","%.4f"%kmse_3," ","%.4f"%(kdi_3*10))


print("")
print("###########################################################################")
print("")
print("Fuzzy C Means Algorithm ...")
print(" ")
import FuzzyCMeans_FINAL
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%fcpi_1," ","%.4f"%fintra_1," ","%.4f"%finter_1," ","%.4f"%fsi_1," ","%.4f"%fmse_1," ","%.4f"%(fdi_1*10))
print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%fcpi_2," ","%.4f"%fintra_2," ","%.4f"%finter_2," ","%.4f"%fsi_2," ","%.4f"%fmse_1," ","%.4f"%(fdi_2*10))
print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%fcpi_3," ","%.4f"%fintra_3," ","%.4f"%finter_3," ","%.4f"%fsi_3," ","%.4f"%fmse_1,"  ","%.4f"%(fdi_3*10))

print("")
print("###########################################################################")
print("")
print("PSO with K-Means Algorithm ...")
import PSO_Kmeans_FINAL1
print(" ")
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%pcpi_1," ","%.4f"%pintra_1," ","%.4f"%pinter_1," ","%.4f"%psi_1," ","%.4f"%pmse_1," ","%.4f"%(pdi_1*10))
import PSO_Kmeans_FINAL2
print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%pcpi_2," ","%.4f"%pintra_2," ","%.4f"%pinter_2," ","%.4f"%psi_2," ","%.4f"%pmse_2," ","%.4f"%(pdi_2*10))
import PSO_Kmeans_FINAL3
print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%pcpi_3," ","%.4f"%pintra_3,"   ","%.4f"%pinter_3,"  ","%.4f"%psi_3,"  ","%.4f"%pmse_3," ","%.4f"%(pdi_3*10))

print("")
print("###########################################################################")
print("")
print("HBPSO with K-Means Algorithm ...")
import HBPSO_Kmeans_FINAL1
print(" ")
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%hcpi_1," ","%.4f"%hintra_1," ","%.4f"%hinter_1," ","%.4f"%hsi_1," ","%.4f"%hmse_1," ","%.4f"%(hdi_1*10))
import HBPSO_Kmeans_FINAL2
print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%hcpi_2," ","%.4f"%hintra_2," ","%.4f"%hinter_2," ","%.4f"%hsi_2," ","%.4f"%hmse_2," ","%.4f"%(hdi_2*10))
import HBPSO_Kmeans_FINAL3
print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%hcpi_3," ","%.4f"%hintra_3,"   ","%.4f"%hinter_3,"  ","%.4f"%hsi_3,"  ","%.4f"%hmse_3," ","%.4f"%(hdi_3*10))



print("")
print("###########################################################################")
print("")
print("GA with K-Means Algorithm ...")
import GA_Kmeans_FINAL1
print(" ")
print("CASE 1 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%gcpi_1," ","%.4f"%gintra_1," ","%.4f"%ginter_1," ","%.4f"%gsi_1," ","%.4f"%gmse_1," ","%.4f"%(gdi_1*10))
import GA_Kmeans_FINAL2
print("")
print("CASE 2 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%gcpi_2," ","%.4f"%gintra_2," ","%.4f"%ginter_2," ","%.4f"%gsi_2," ","%.4f"%gmse_2," ","%.4f"%(gdi_2*10))
import GA_Kmeans_FINAL3
print("")
print("CASE 3 ------------------------------")
print("CPI       INTRA       INTER      SC       MSE      DUNN")
print("%.4f"%gcpi_3," ","%.4f"%gintra_3,"   ","%.4f"%ginter_3,"  ","%.4f"%gsi_3,"  ","%.4f"%gmse_3," ","%.4f"%(gdi_3*10))

'''
kcpix = [1,2,3]
#kcpiy = [kcpi_1,kpci_2,kcpi_3]
kcpiy =[0.6474,0.6371,0.857]
fcpix = [1,2,3]
#fcpiy =[fcpi_1,fcpi_2,fcpi_3]
fcpiy =[0.6602,0.6666,0.8579]
pcpix=[1,2,3]
#pcpiy = [pcpi_1,pcpi_2,pcpi_3]
pcpiy =[0.6397,0.6475,0.8589]
gcpix = [1,2,3]
#gcpiy = [gcpi_1,gcpi_2,gcpi_3]
gcpiy=[0.6397,0.6474,0.8589]
plt.scatter(kcpix,kcpiy,s=30,c="blue",label="KMeans")
plt.plot(kcpix,kcpiy,c="blue")
plt.scatter(fcpix,fcpiy,s=30,c="green",label="FuzzyCMeans")
plt.plot(fcpix,fcpiy,c="green")
plt.scatter(pcpix,pcpiy,s=130,c="red",label="PSO")
plt.plot(pcpix,pcpiy,c="red")
plt.scatter(gcpix,gcpiy,s=30,c="yellow",label="GA")
plt.plot(gcpix,gcpiy,c="yellow")
plt.title("CPI")
plt.legend()
plt.show()

kintrax = [1,2,3]
#kintray = [kintra_1,kintra_2,kintra_3]
kintray = [727.41,702.16,708.51]
fintrax = [1,2,3]
#fintray =[fintra_1,fintra_2,fintra_3]
fintray =[747.65,722.58,717.70]
pintrax=[1,2,3]
#pintray = [pintra_1,pintra_2,pintra_3]
pintray =[722.85,689.52,720.25]
gintrax = [1,2,3]
#gintray = [gintra_1,gintra_2,gintra_3]
gintray = [722.85,689.52,720.25]
plt.scatter(kintrax,kintray,s=30,c="blue",label="KMeans")
plt.plot(kintrax,kintray,c="blue")
plt.scatter(fintrax,fintray,s=30,c="green",label="FuzzyCMeans")
plt.plot(fintrax,fintray,c="green")
plt.scatter(pintrax,pintray,s=130,c="red",label="PSO")
plt.plot(pintrax,pintray,c="red")
plt.scatter(gintrax,gintray,s=30,c="yellow",label="GA")
plt.plot(gintrax,gintray,c="yellow")
plt.title("Intra")
plt.legend()
plt.show()

kinterx = [1,2,3]
#kintery = [kinter_1,kinter_2,kinter_3]
kintery = [2249.39,2190.65,196.69 ]
finterx = [1,2,3]
#fintery =[finter_1,finter_2,finter_3]
fintery =[2218.03,2221.34,870.75]
pinterx=[1,2,3]
#pintery = [pinter_1,pinter_2,pinter_3]
pintery =[2453.15,2640.71,1952.65]
ginterx = [1,2,3]
#gintery = [ginter_1,ginter_2,ginter_3]
gintery =[2453.15,2640.71,1952.65]
plt.scatter(kinterx,kintery,s=30,c="blue",label="KMeans")
plt.plot(kinterx,kintery,c="blue")
plt.scatter(finterx,fintery,s=30,c="green",label="FuzzyCMeans")
plt.plot(finterx,fintery,c="green")
plt.scatter(pinterx,pintery,s=130,c="red",label="PSO")
plt.plot(pinterx,pintery,c="red")
plt.scatter(ginterx,gintery,s=30,c="yellow",label="GA")
plt.plot(ginterx,gintery,c="yellow")
plt.title("Inter")
plt.legend()
plt.show()

ksix = [1,2,3]
#ksiy = [ksi_1,ksi_2,ksi_3]
ksiy=[0.5349,0.5463,0.6009]
fsix = [1,2,3]
#fsiy =[fsi_1,fsi_2,fsi_3]
fsiy=[0.5164,0.5323,0.5926]
psix=[1,2,3]
#psiy = [psi_1,psi_2,psi_3]
psiy =[0.5537,0.5893,0.5967]
gsix = [1,2,3]
#gsiy = [gsi_1,gsi_2,gsi_3]
gsiy =[0.5537,0.5893,0.5967]
plt.scatter(ksix,ksiy,s=30,c="blue",label="KMeans")
plt.plot(ksix,ksiy,c="blue")
plt.scatter(fsix,fsiy,s=30,c="green",label="FuzzyCMeans")
plt.plot(fsix,fsiy,c="green")
plt.scatter(psix,psiy,s=130,c="red",label="PSO")
plt.plot(psix,psiy,c="red")
plt.scatter(gsix,gsiy,s=30,c="yellow",label="GA")
plt.plot(gsix,gsiy,c="yellow")
plt.title("Silhoutte Coefficient")
plt.legend()
plt.show()

kmsex = [1,2,3]
#kmsey = [kmse_1,kmse_2,kmse_3]
kmsey=[1454.82,1404.32,-354.25]
fmsex = [1,2,3]
#fmsey =[fmse_1,fmse_2,fmse_3]
fmsey=[1464.73,1451.89,358.85]
pmsex=[1,2,3]
#pmsey = [pmse_1,pmse_2,pmse_3]
pmsey=[1445.7,1379.04,360.12]
gmsex = [1,2,3]
#gmsey = [gmse_1,gmse_2,gmse_3]
gmsey =[1445.7,1379.04,360.12]
plt.scatter(kmsex,kmsey,s=30,c="blue",label="KMeans")
plt.plot(kmsex,kmsey,c="blue")
plt.scatter(fmsex,fmsey,s=30,c="green",label="FuzzyCMeans")
plt.plot(fmsex,fmsey,c="green")
plt.scatter(pmsex,pmsey,s=130,c="red",label="PSO")
plt.plot(pmsex,pmsey,c="red")
plt.scatter(gmsex,gmsey,s=30,c="yellow",label="GA")
plt.plot(gmsex,gmsey,c="yellow")
plt.title("MSE")
plt.legend()
plt.show()

kdix = [1,2,3]
#kdiy = [kdi_1*10,kdi_2*10,kdi_3*10]
kdiy =[0.0214,0.0113,0.0187]
fdix = [1,2,3]
#fdiy =[fdi_1*10,fdi_2*10,fdi_3*10]
fdiy =[0.0047,0.0055,0.0106]
pdix=[1,2,3]
#pdiy = [pdi_1*10,pdi_2*10,pdi_3*10]
pdiy=[]
gdix = [1,2,3]
#gdiy = [gdi_1*10,gdi_2*10,gdi_3*10]
gdiy = [0.0453,0.0269,0.0187]
plt.scatter(kdix,kdiy,s=30,c="blue",label="KMeans")
plt.plot(kdix,kdiy,c="blue")
plt.scatter(fdix,fdiy,s=30,c="green",label="FuzzyCMeans")
plt.plot(fdix,fdiy,c="green")
plt.scatter(pdix,pdiy,s=140,c="red",label="PSO")
plt.plot(pdix,pdiy,c="red")
plt.scatter(gdix,gdiy,s=30,c="yellow",label="GA")
plt.plot(gdix,gdiy,c="yellow")
plt.title("Dunn Index")
plt.legend()
plt.show()
'''