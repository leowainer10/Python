
albuns={
    "Encore" :['1','Curtains Up', ' ', '00:47'],
    "Encore" :['2','Evil Deeds','Dr. Dre' ,'4:20'],
    "Encore" :['3','Never Enough (feat. Nate Dogg, 50 Cent)','Dr. Dre, Mike Elizondo' ,'2:40'],
    "Encore" :['4','Yellow Brick Road','Eminem, Luis Resto' ,'5:46'],
    "Encore" :['5','Like Toy Soldiers','Eminem, Luis Resto' ,'4:57'],
    "Encore" :['6','Mosh','Dr. Dre, Mark Batson' ,'5:18'],
    "Encore" :['7','Puke','Eminem, Luis Resto' ,'4:08'],
    "Encore" :['8','My 1st Single','Eminem, Luis Resto' ,'5:03'],
    "Encore" :['9','Paul',' ','0:32'],
    "Encore" :['10','Rain Man','Dr. Dre' ,'5:14'],
    "Encore" :['11','Big Weenie','Dr. Dre' ,'4:27'],
    "Encore" :['12','Em Calls Paul',' ','1:12'],
    "Encore" :['13','Just Lose It','Dr. Dre, Mike Elizondo' ,'4:09'],
    "Encore" :['14','Ass Like That','Dr. Dre, Mike Elizondo' ,'4:26'],
    "Encore" :['15','Spend Some Time (feat. Obie Trice, Stat Quo, 50 Cent)','Eminem, Luis Resto' ,'5:11'],
    "Encore" :['16','Mockingbird','Eminem, Luis Resto' ,'4:11'],
    "Encore" :['17','Crazy in Love','Eminem, Luis Resto' ,'4:02'],
    "Encore" :['18','One Shot 2 Shot (feat. D12)','Eminem, Luis Resto' ,'4:27'],
    "Encore" :['19','Final Thought',' ','0:30'],
    "Encore" :['20','Encore/Curtains Down (feat. Dr. Dre, 50 Cent)','Dr. Dre, Mark Batson' ,'5:48'],
}


encore ={
    '1' :[ "Curtains Up",'','0:47'],
    '2' :[ "Evil Deeds",'Dr. Dre', '4:20'],
    '3' :[ "Never Enough (feat. Nate Dogg, 50 Cent)",'Dr. Dre, Mike Elizondo','2:40'],
    '4' :[ "Yellow Brick Road",'Eminem, Luis Resto','5:46'],
    '5' :[ "Like Toy Soldiers",'Eminem, Luis Resto','4:57'],
    '6' :[ "Mosh",'Dr. Dre, Mark Batson','5:18'],
    '7' :[ "Puke",'Eminem, Luis Resto','4:08'],
    '8' :[ "My 1st Single",'Eminem, Luis Resto','5:03'],
    '9' :[ "Paul",'','0:32'],
    '10':[ "Rain Man",'Dr. Dre', '5:14'],
    '11':[ "Big Weenie",'Dr. Dre', '4:27'],
    '12':[ "Em Calls Paul",'','1:12'],
    '13':[ "Just Lose It",'Dr. Dre, Mike Elizondo','4:09'],
    '14':[ "Ass Like That",'Dr. Dre, Mike Elizondo','4:26'],
    '15':[ "Spend Some Time (feat. Obie Trice, Stat Quo, 50 Cent)",'Eminem, Luis Resto','5:11'],
    '16':[ "Mockingbird",'Eminem, Luis Resto','4:11'],
    '17':[ "Crazy in Love",'Eminem, Luis Resto','4:02'],
    '18':[ "One Shot 2 Shot (feat. D12)",'Eminem, Luis Resto','4:27'],
    '19':[ "Final Thought",'','0:30'],
    '20':[ "Encore/Curtains Down (feat. Dr. Dre, 50 Cent)",'Dr. Dre, Mark Batson','5:48'],
}


# for i in range(len(encore)):
    # print(encore.items[i][1])
    # encore.items


for x in encore:
  print( '"' +str(encore[x][0]) + '"' + ' | ' + str(encore[x][1]) + ' | With the total duration of: ' + str(encore[x][2]) + '.') 
 