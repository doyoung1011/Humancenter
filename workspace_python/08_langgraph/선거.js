// 문제


let names = ['이순신장군님','규혁', '정과장님', '영욱', '상우', '용준', '도영', '재성', '변준석가모니','킹갓최민수강사님','차수원장님']

// 1. 랜덤으로 1명을 고른다
// 2. 1.의 행동을 100번 반복한다
// 3. 누가 몇표가 나왔는지 출력한다
// 4. 가장 많은 득표수는 누구, 몇표만 출력한다


//   득표수 체크 
    let votes=[]; // 득표수를 담을 빈 배열 생성
    for(let i=0; i<names.length;i++){
       votes[i]=0
    }
    // 여기는 랜덤 투표하는곳
    for(j=0;j<100;j++){
        let random=Math.floor(Math.random()*names.length)
        votes[random]++
  
    }
  console.log('전체 투표 결과는?')
  for(let k=0;k<names.length;k++){
      console.log(`${names[k]}: ${votes[k]}표`);

  }
//   최다 득표수와 몇 표인지 체크할려고 만들어둠
  let highVoteCount=votes[0] // 최다 득표수 비교시점
  let lowCount=votes[0] // 최소 득표수 비교시점
  let highMan=-1 // 최다 득표 되실분
  let lowMan=null // 최소 득표되신분

  console.log('--------')
  for(let m=0;m<names.length;m++){
    if(votes[m]>highVoteCount){
        highVoteCount=votes[m]
        highMan=m

    }
    if(votes[m]<lowCount){
        lowCount=votes[m]
        lowMan=m
    }

  }
  console.log('최다 득표자수는?')
  console.log(names[highMan],highVoteCount)
  console.log('최저 표 받으신분은?')
  console.log(names[lowMan],lowCount)

  
  
  /*
  인덱스가 같다는 전제 하에 하는거라서 json을 이용해서 활용해보자

  */

//   const name=['규혁', '정과장님', '영욱', '상우', '용준', '도영', '재성', '변준석가모니','킹갓최민수강사님','차수원장님']
  
//   let idx=Math.random()*name.