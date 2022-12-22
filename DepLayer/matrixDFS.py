# import numpy
# import numpy as np
# import numpy.ma as ma
# from depLayer import *


# cLevel = MBs_classes
# countZones[cLevel]=countZones(cLevel) + 1
# zoneList[cLevel][countZones(cLevel)]=[]
# zoneList[cLevel][countZones(cLevel)]=[]
# # matrixDFS.m:5
#     nextMB=concat([nIndex,mIndex])
# # matrixDFS.m:7
#     stackMB[end() + 1,arange()]=nextMB
# # matrixDFS.m:8
#     markedMBs[nextMB(1),nextMB(2)]=cLevel
# # matrixDFS.m:9
#     #Mark the zone
#     while (logical_not(isempty(stackMB))):

#         n=stackMB(1,1)
# # matrixDFS.m:13
#         m=stackMB(1,2)
# # matrixDFS.m:14
#         zoneList[cLevel][countZones(cLevel)][end() + 1,arange()]=concat([n,m])
# # matrixDFS.m:17
#         #col - m
#         #Adjancecy
#     ##
#     #SEQUENTIAL ORDER
#         if (m + 1 <= M and (markedMBs(n,m + 1) == 0) and (MBs_classes(n,m + 1) == cLevel)):
#             markedMBs[n,m + 1]=cLevel
# # matrixDFS.m:26
#             stackMB=concat([[stackMB],[concat([n,m + 1])]])
# # matrixDFS.m:27
#         if (n + 1 <= N and m + 1 <= M and (markedMBs(n + 1,m + 1) == 0) and (MBs_classes(n + 1,m + 1) == cLevel)):
#             markedMBs[n + 1,m + 1]=cLevel
# # matrixDFS.m:31
#             stackMB=concat([[stackMB],[concat([n + 1,m + 1])]])
# # matrixDFS.m:32
#         if (n + 1 <= N and (markedMBs(n + 1,m) == 0) and (MBs_classes(n + 1,m) == cLevel)):
#             markedMBs[n + 1,m]=cLevel
# # matrixDFS.m:36
#             stackMB=concat([[stackMB],[concat([n + 1,m])]])
# # matrixDFS.m:37
#         if (n + 1 <= N and m - 1 >= 1 and (markedMBs(n + 1,m - 1) == 0) and (MBs_classes(n + 1,m - 1) == cLevel)):
#             markedMBs[n + 1,m - 1]=cLevel
# # matrixDFS.m:41
#             stackMB=concat([[stackMB],[concat([n + 1,m - 1])]])
# # matrixDFS.m:42
#         if (m - 1 >= 1 and (markedMBs(n,m - 1) == 0) and (MBs_classes(n,m - 1) == cLevel)):
#             markedMBs[n,m - 1]=cLevel
# # matrixDFS.m:46
#             stackMB=concat([[stackMB],[concat([n,m - 1])]])
# # matrixDFS.m:47
#         if (n - 1 >= 1 and m - 1 >= 1 and (markedMBs(n - 1,m - 1) == 0) and (MBs_classes(n - 1,m - 1) == cLevel)):
#             markedMBs[n - 1,m - 1]=cLevel
# # matrixDFS.m:51
#             stackMB=concat([[stackMB],[concat([n - 1,m - 1])]])
# # matrixDFS.m:52
#         if (n - 1 >= 1 and (markedMBs(n - 1,m) == 0) and (MBs_classes(n - 1,m) == cLevel)):
#             markedMBs[n - 1,m]=cLevel
# # matrixDFS.m:56
#             stackMB=concat([[stackMB],[concat([n - 1,m])]])
# # matrixDFS.m:57
#         if (n - 1 >= 1 and m + 1 <= M and (markedMBs(n - 1,m + 1) == 0) and (MBs_classes(n - 1,m + 1) == cLevel)):
#             markedMBs[n - 1,m + 1]=cLevel
# # matrixDFS.m:61
#             stackMB=concat([[stackMB],[concat([n - 1,m + 1])]])
# ##########################
# #### AQUI##########
# ###################


# # matrixDFS.m:62
#         #######################################################################
#     ##
#     #SMART ORDER
#     # if(m+1<=M && (markedMBs(n, m+1)==0) && (MBs_classes(n, m+1)==cLevel) )
#     #     markedMBs(n, m+1) = cLevel;
#     #     stackMB = [stackMB; [n, m+1]];
#     # end
#     # 
#     # if(n+1<=N && m-1>=1 && (markedMBs(n+1, m-1)==0) && (MBs_classes(n+1, m-1)==cLevel) )
#     #     markedMBs(n+1, m-1) = cLevel;
#     #     stackMB = [stackMB; [n+1, m-1]];
#     # end
#     # 
#     # if(n+1<=N && (markedMBs(n+1, m)==0) && (MBs_classes(n+1, m)==cLevel) )
#     #     markedMBs(n+1, m) = cLevel;
#     #     stackMB = [stackMB; [n+1, m]];
#     # end
#     # 
#     # if(n+1<=N && m+1<=M && (markedMBs(n+1, m+1)==0) && (MBs_classes(n+1, m+1)==cLevel) )
#     #     markedMBs(n+1, m+1) = cLevel;
#     #     stackMB = [stackMB; [n+1, m+1]];
#     # end
#     # 
#     # if(m-1>=1 && (markedMBs(n, m-1)==0) && (MBs_classes(n, m-1)==cLevel) )
#     #     markedMBs(n, m-1) = cLevel;
#     #     stackMB = [stackMB; [n, m-1]];
#     # end
#     # 
#     # if(n-1>=1 && m-1>=1 && (markedMBs(n-1, m-1)==0) && (MBs_classes(n-1, m-1)==cLevel) )
#     #     markedMBs(n-1, m-1) = cLevel;
#     #     stackMB = [stackMB; [n-1, m-1]];
#     # end
#     # 
#     # if(n-1>=1 && (markedMBs(n-1, m)==0) && (MBs_classes(n-1, m)==cLevel) )
#     #     markedMBs(n-1, m) = cLevel;
#     #     stackMB = [stackMB; [n-1, m]];
#     # end
#     # 
#     # if(n-1>=1 && m+1<=M && (markedMBs(n-1, m+1)==0) && (MBs_classes(n-1, m+1)==cLevel) )
#     #     markedMBs(n-1, m+1) = cLevel;
#     #     stackMB = [stackMB; [n-1, m+1]];
#     # end
#         #######################################################################
#     ##
#         stackMB=stackMB(arange(2,end()),arange())
# # matrixDFS.m:111