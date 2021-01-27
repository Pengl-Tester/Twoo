// 定义测试场景文件路径变量
// def testplan="./auto/plan/DatabaseTest/test_evcall01.py"

// 声明式 pipeline 替代node
node {
    // init Python 运行环境
    // 初始化一些运行态需要的全局变量
    stage("Init"){
        echo "Init Run Env"
        sh 'python3 --version'
    }

    // 从git获取最新代码
    stage("Check out"){
        echo "check out last code"
        checkout scm
    }

    // 启动测试
    stage("Test"){
        sh "pytest --version"
        dir("."){
            sh "pwd"
            sh "cd ./auto/plan/DatabaseTest/"
            // sh "pytest ${testplan} --html=./logs/report.html --self-contained-html"
            sh "pytest  --cache-clear --html=./logs/report.html --self-contained-html"
            // sh "pytest"
        }
    }
    
    // 发布html报告
    stage("Report"){
        dir("."){
            publishHTML(target: [
                alowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'logs',
                reportFiles: 'report.html',
                reportName: "HTML Report"
            ]
            )
        }
    }

    stage("Notify"){
        script{
            if(currentBuild.currentResult == "SUCCESS"){
                // build success,do nothing
                echo "It's build SUCCESS"
                dingTalk (robot: "a0aed95d-d00a-4210-b78c-62dee56a7e0f", type: "TEXT", at:["18203017916"], atAll:false, title: "${currentBuild.projectName} BUILD ${currentBuild.currentResult}!",text: ["项目:${currentBuild.projectName}", "构建号:#${currentBuild.number}","结果:${currentBuild.currentResult}\n"], messageUrl: "http://192.168.2.197:8081/job/EVCALL-AUTO-TEST/", picUrl:'https://images.669pic.com/element_min_new_pic/60/25/33/43/a59876e1871d8119f88a7557d611869e.png', singleTitle:'',btns: [], hideAvatar: false)
            }
            else{
                // build failure or abort send dingTalk
                echo "It's build Faild"
                dingTalk (robot: "a0aed95d-d00a-4210-b78c-62dee56a7e0f", type: "TEXT", at:["18203017916"], atAll:true, title: "${currentBuild.projectName} BUILD ${currentBuild.currentResult}!",text: ["项目:${currentBuild.projectName}", "构建号:#${currentBuild.number}","结果:${currentBuild.currentResult}\n"], messageUrl: "http://192.168.2.197:8081/job/EVCALL-AUTO-TEST/", picUrl:'https://img95.699pic.com/element/40136/9148.png_300.png', singleTitle:'',btns: [], hideAvatar: false)          
                     
            }
        }
    }
}