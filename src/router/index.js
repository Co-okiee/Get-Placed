import { createRouter, createWebHistory } from "vue-router";
// Import necessary components
import Dashboard from "../views/Dashboard.vue"; // Dashboard as home component
import Study from "../views/Study.vue"; // Study page component
import DataStructures from "../views/DataStructures.vue"; // Data Structures page component
import Arrays from "../views/Arrays.vue"; // Arrays page component
import Matrix from "../views/Matrix.vue";
import Strings from "../views/Strings.vue"; // Matrix page component
import Login from "../views/Login.vue"; // Login page component
import Signup from "../views/Signup.vue"; // Signup page component
import NotFound from "../views/NotFound.vue"; // Not Found page component
import CompanyCodingPage from "../views/CompanyCodingPage.vue";
import QuizOptions from "../views/QuizOptions.vue";
import TopicWise from "../views/TopicWise.vue";
import ArrayQuiz from "../views/ArrayQuiz.vue";
import MockInterview from "../views/MockInterview.vue";
import UploadResume from "../views/UploadResume.vue";
import VideoCapture from "../views/VideoCapture.vue";

// Data Structures Related Imports
import LinkedLists from "../views/LinkedLists.vue";
import Stack from "../views/Stack.vue";
import Queue from "../views/Queue.vue";
import Tree from "../views/Tree.vue";
import Graph from "../views/Graph.vue";
import Hashing from "../views/Hashing.vue";
import Heap from "../views/Heap.vue";
import ADS from "../views/ADS.vue";
import Map from "../views/Map.vue";
import Set from "../views/Set.vue";

// Algorithms Related Imports
import Algorithms from "../views/Algorithms.vue";
import AnalysisofAlgo from "../views/AnalysisofAlgo.vue";
import Searching from "../views/Searching.vue";
import Sorting from "../views/Sorting.vue";
import DivideandConquer from "../views/DivideandConquer.vue";
import MathematicalAlgorithms from "../views/MathematicalAlgorithms.vue";
import GreedyAlgo from "../views/GreedyAlgo.vue";
import DP from "../views/DP.vue";
import Geometric from "../views/Geometric.vue";
import GraphAlgo from "../views/GraphAlgo.vue";
import Pattern from "../views/Pattern.vue";
import Recursion from "../views/Recursion.vue";
import Bitwise from "../views/Bitwise.vue";
import Backtracking from "../views/Backtracking.vue";
import Randomised from "../views/Randomised.vue";
import BranchBound from "../views/BranchBound.vue";

// Operating Systems Related Imports
import OS from "../views/OS.vue";
import Basics from "../views/Basics.vue";
import SystemStructure from "../views/SystemStructure.vue";
import CPU from "../views/CPU.vue";
import ProcessSyn from "../views/ProcessSyn.vue";
import Deadlock from "../views/Deadlock.vue";
import ProcessThreads from "../views/ProcessThreads.vue";
import Memory from "../views/Memory.vue";
import Disk from "../views/Disk.vue";
import Misc from "../views/Misc.vue";

// DBMS and OOPS Related Imports
import DBMS from "../views/DBMS.vue";
import OOPS from "../views/OOPS.vue";
import BasicsOOPS from "../views/BasicsOOPS.vue";
import Encapsulation from "../views/Encapsulation.vue";
import Abstraction from "../views/Abstraction.vue";
import Polymorphism from "../views/Polymorphism.vue";
import Inheritance from "../views/Inheritance.vue";
import DynamicBinding from "../views/DynamicBinding.vue";

// Computer Networks Related Imports
import CN from "../views/CN.vue";
import CNBasics from "../views/CNBasics.vue";
import DataLinkLayer from "../views/DataLinkLayer.vue";
import NetworkLayer from "../views/NetworkLayer.vue";
import TransportLayer from "../views/TransportLayer.vue";
import ApplicationLayer from "../views/ApplicationLayer.vue";
import NetworkSecurity from "../views/NetworkSecurity.vue";
import CompressionTech from "../views/CompressionTech.vue";
import NetworkExp from "../views/NetworkExp.vue";
import Devices from "../views/Devices.vue";
import CNMisc from "../views/CNMisc.vue";

// System Design Related Imports
import SystemDesign from "../views/SystemDesign.vue";
import BasicsSystem from "../views/BasicsSystem.vue";
import Scalibility from "../views/Scalibility.vue";
import Database from "../views/Database.vue";
import HLD from "../views/HLD.vue";
import LLD from "../views/LLD.vue";

// Other Specific Imports
import AptandResoning from "../views/AptandResoning.vue";
import TrackProgress from "../views/TrackProgress.vue";
import Verbalquizes from "../views/Verbalquizes.vue";
import VAQuizPage from "../views/VAQuizPage.vue";
import CompanySpecific from '../views/CompanySpecific.vue';

// Company Landing Pages
import BarclaysLanding from '../views/BarclaysLanding.vue';
import DeutscheBankLanding from '../views/DeutscheBankLanding.vue';
import JPMorganLanding from '../views/JPMorganLanding.vue';
import AccentureLanding from '../views/AccentureLanding.vue';
import TCSLanding from '../views/TCSLanding.vue';
import OracleLanding from '../views/OracleLanding.vue';
import WiproLanding from '../views/WiproLanding.vue';
import CognizantLanding from '../views/CognizantLanding.vue';
import GoogleLanding from '../views/GoogleLanding.vue';
import MicrosoftLanding from '../views/MicrosoftLanding.vue';
import AmazonLanding from '../views/AmazonLanding.vue';
import SiemensLanding from '../views/SiemensLanding.vue';
import NvidiaLanding from '../views/NvidiaLanding.vue';
import DeloitteLanding from '../views/DeloitteLanding.vue';
import AirtelLanding from '../views/AirtelLanding.vue';

// Additional Specific Imports
import CodingIde from '../views/CodingIde.vue';
import MockExamBarclays from "../views/MockExamBarclays.vue";
import AutomataPage from '../views/AutomataPage.vue';

// Quiz Related Imports
import AlgoQuiz from "../views/AlgoQuiz.vue";
import OSQuiz from "../views/OSQuiz.vue";
import DBMSQuiz from "../views/DBMSQuiz.vue";
import OOPSQuiz from "../views/OOPSQuiz.vue";
import AptQuiz from "../views/AptQuiz.vue";
import CNTQuiz from "../views/CNTQuiz.vue";
import SystemDQuiz from "../views/SystemDQuiz.vue";

// AI Related Imports
import Aidatastructure from "../views/aidatastructure.vue";
import AiTopicwise from "../views/AiTopicwise.vue";

// Create router instance
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/", // Home path
      name: "home",
      component: Dashboard, // Dashboard as the home component
    },
    {
      path: "/login",
      name: "login",
      component: Login, // Login page component
    },
    {
      path: "/signup",
      name: "signup",
      component: Signup, // Signup page component
    },
    {
      path: "/mock-interview",
      name: "mock-interview",
      component: MockInterview, // Mock Interview page component
    },
    {
      path: "/study",
      name: "study",
      component: Study, // Study page component
    },
    {
      path: "/data-structures",
      name: "data-structures",
      component: DataStructures, // Data Structures page component
    },
    {
      path: "/aidatastructure",
      name: "aidatastructure",
      component: Aidatastructure, // Data Structures page component
    },
    {
      path: "/aitopicwise",
      name: "aitopicwise",
      component: AiTopicwise, //Ai
    },
    
    {
      path: "/arrays",
      name: "arrays",
      component: Arrays, // Arrays page component
    },
    {
      path: "/matrix",
      name: "matrix",
      component: Matrix, // Matrix page component
    },
    {
      path: "/upload-resume",
      name: "upload-resume",
      component: UploadResume, // Upload Resume component
    },
    {
      path: "/video-capture",
      name: "video-capture",
      component: VideoCapture, // Ensure this path is correct
    },
    {
      path: '/strings', // Add this route for the Matrix component
      name: 'strings',
      component: Strings,
    },
    {
      path: '/linkedlists', // Add this route for the Matrix component
      name: 'linkedlists',
      component: LinkedLists,
    },
    {
      path: '/stack', // Add this route for the Matrix component
      name: 'stack',
      component: Stack,
    },
    {
      path: '/queue', // Add this route for the Matrix component
      name: 'queue',
      component: Queue,
    },
    {
      path: '/tree', // Add this route for the Matrix component
      name: 'tree',
      component: Tree,
    },
    {
      path: '/heap', // Add this route for the Matrix component
      name: 'heap',
      component: Heap,
    },
    {
      path: '/hashing', // Add this route for the Matrix component
      name: 'hashing',
      component: Hashing,
    },
    {
      path: '/graph', // Add this route for the Matrix component
      name: 'graph',
      component: Graph,
    },
    {
      path: '/set', // Add this route for the Matrix component
      name: 'set',
      component: Set,
    },
    {
      path: '/map', // Add this route for the Matrix component
      name: 'map',
      component: Map,
    },
    
    {
      path: '/ADS', // Add this route for the Matrix component
      name: 'ADS',
      component: ADS,
    },
    {
      path: '/algorithms', // Add this route for the Matrix component
      name: 'algorithms',
      component: Algorithms,
    },
    {
      path: '/analysisofalgo', // Add this route for the Matrix component
      name: 'analysisofalgo',
      component: AnalysisofAlgo,
    },
    {
      path: '/searching', // Add this route for the Matrix component
      name: 'searching',
      component: Searching,
    },
    {
      path: '/sorting', // Add this route for the Matrix component
      name: 'sorting',
      component: Sorting,
    },
    {
      path: '/divide-and-conquer', // Add this route for the Matrix component
      name: 'divide-and-conquer',
      component: DivideandConquer,
    },
    {
      path: '/mathematical-algo', // Add this route for the Matrix component
      name: 'mathematical-algo',
      component: MathematicalAlgorithms,
    },
    {
      path: '/greedy', // Add this route for the Matrix component
      name: 'greedy',
      component: GreedyAlgo,
    },
    {
      path: '/dynamic', // Add this route for the Matrix component
      name: 'dynamic',
      component: DP,
    },
    {
      path: '/geometric', // Add this route for the Matrix component
      name: 'geometric',
      component: Geometric,
    },
    {
      path: '/graphalgo', // Add this route for the Matrix component
      name: 'graphalgo',
      component: GraphAlgo,
    },
    {
      path: '/pattern', // Add this route for the Matrix component
      name: 'pattern',
      component: Pattern,
    },
    {
      path: '/recursion', // Add this route for the Matrix component
      name: 'recursion',
      component: Recursion,
    },
    {
      path: '/bitwise', // Add this route for the Matrix component
      name: 'bitwise',
      component: Bitwise,
    },
    {
      path: '/backtracking', // Add this route for the Matrix component
      name: 'backtracking',
      component: Backtracking,
    },
    {
      path: '/randomised', // Add this route for the Matrix component
      name: 'randomised',
      component: Randomised,
    },
    {
      path: '/branchbound', // Add this route for the Matrix component
      name: 'branchbound',
      component: BranchBound,
    },
    {
      path: '/os', // Add this route for the Matrix component
      name: 'os',
      component: OS,
    },
    {
      path: '/basics', // Add this route for the Matrix component
      name: 'basics',
      component: Basics,
    },
    {
      path: '/system', // Add this route for the Matrix component
      name: 'system',
      component: SystemStructure,
    },
    {
      path: '/CPU', // Add this route for the Matrix component
      name: 'CPU',
      component: CPU,
    },
    {
      path: '/processsyn', // Add this route for the Matrix component
      name: 'processsyn',
      component: ProcessSyn,
    },
    {
      path: '/deadlock', // Add this route for the Matrix component
      name: 'deadlock',
      component: Deadlock,
    },
    {
      path: '/pt', // Add this route for the Matrix component
      name: 'pt',
      component: ProcessThreads,
    },
    {
      path: '/memory', // Add this route for the Matrix component
      name: 'memory',
      component: Memory,
    },
    {
      path: '/disk', // Add this route for the Matrix component
      name: 'disk',
      component: Disk,
    },
    {
      path: '/misc', // Add this route for the Matrix component
      name: 'misc',
      component: Misc,
    },
    {
      path: '/dbms', // Add this route for the Matrix component
      name: 'dbms',
      component: DBMS,
    },
    {
      path: '/oops', // Add this route for the Matrix component
      name: 'oops',
      component: OOPS,
    },
    {
      path: '/OOPSbasic', // Add this route for the Matrix component
      name: 'OOPSbasic',
      component: BasicsOOPS,
    },
    {
      path: '/encapsulation', // Add this route for the Matrix component
      name: 'encapsulation',
      component: Encapsulation,
    },
    {
      path: '/abstraction', // Add this route for the Matrix component
      name: 'abstraction',
      component: Abstraction,
    },
    {
      path: '/polymorphism', // Add this route for the Matrix component
      name: 'polymorphism',
      component: Polymorphism,
    },
    {
      path: '/inhertance', // Add this route for the Matrix component
      name: 'inheritance',
      component: Inheritance,
    },
    {
      path: '/dynamicbinding', // Add this route for the Matrix component
      name: 'dynamicbinding',
      component: DynamicBinding,
    },
    {
      path: '/CN', // Add this route for the Matrix component
      name: 'CN',
      component: CN,
    },
    {
      path: '/CNbasics', // Add this route for the Matrix component
      name: 'CNbasics',
      component: CNBasics,
    },
    {
      path: '/datalink', // Add this route for the Matrix component
      name: 'datalink',
      component: DataLinkLayer,
    },
    {
      path: '/network', // Add this route for the Matrix component
      name: 'network',
      component: NetworkLayer,
    },
    {
      path: '/transport', // Add this route for the Matrix component
      name: 'transport',
      component: TransportLayer,
    },
    {
      path: '/application', // Add this route for the Matrix component
      name: 'application',
      component: ApplicationLayer,
    },
    {
      path: '/networksecurity', // Add this route for the Matrix component
      name: 'networksecurity',
      component: NetworkSecurity,
    },
    {
      path: '/compressiontech', // Add this route for the Matrix component
      name: 'compressiontech',
      component: CompressionTech,
    },
    {
      path: '/networkexp', // Add this route for the Matrix component
      name: 'networkexp',
      component: NetworkExp,
    },
    {
      path: '/devices', // Add this route for the Matrix component
      name: 'devices',
      component: Devices,
    },
    {
      path: '/CNmisc', // Add this route for the Matrix component
      name: 'CNmisc',
      component: CNMisc,
    },
    {
      path: '/SystemDesign', // Add this route for the Matrix component
      name: 'SystemDesign',
      component: SystemDesign,
    },
    {
      path: '/BasicsSystem', // Add this route for the Matrix component
      name: 'BasicsSystem',
      component: BasicsSystem,
    },
    {
      path: '/scalability', // Add this route for the Matrix component
      name: 'scalability',
      component: Scalibility,
    },
    {
      path: '/database', // Add this route for the Matrix component
      name: 'database',
      component: Database,
    },
    {
      path: '/HLD', // Add this route for the Matrix component
      name: 'HLD',
      component: HLD,
    },
    {
      path: '/LLD', // Add this route for the Matrix component
      name: 'LLD',
      component: LLD,
    },
    {
      path: '/Apt', // Add this route for the Matrix component
      name: 'Apt',
      component: AptandResoning,
    },


    {
      path: "/topic-wise-quiz",
      name: "topic-wise-quiz",
      component: TopicWise, // Topic Wise Quiz page component
    },
    {
      path: "/quiz-options",
      name: "quiz-options",
      component: QuizOptions, // Quiz Options component
    },

    // Quiz Routes
    {
      path: "/algo_quiz",
      name: "algo_quiz",
      component: AlgoQuiz,
    },
    {
      path: "/os_quiz",
      name: "os_quiz",
      component: OSQuiz,
    },
    {
      path: "/dbms_quiz",
      name: "dbms_quiz",
      component: DBMSQuiz,
    },
    {
      path: "/oops_quiz",
      name: "oops_quiz",
      component: OOPSQuiz,
    },
    {
      path: "/apt_quiz",
      name: "apt_quiz",
      component: AptQuiz,
    },
    {
      path: "/cnt_quiz",
      name: "cnt_quiz",
      component: CNTQuiz,
    },
    {
      path: "/systemd_quiz",
      name: "systemd_quiz",
      component: SystemDQuiz,
    },
    {
      path: "/array-quiz",
      name: "array-quiz",
      component: ArrayQuiz,
    },
    {
      path: "/company-coding",
      name: "company-coding",
      component: CompanyCodingPage,
    },
    {
      path: "/trackprogress",
      name: "trackprogress",
      component: TrackProgress,
    },
    {
      path: "/signup",
      name: "signup",
      component: Signup,
    },
    {
      path: "/question/:id",
      name: "question",
      component: () => import("../views/Question.vue"),
    },
    {
      path: "/quiz-options",
      name: "quiz-options",
      component: QuizOptions,
    },
    {
      path: "/verbalquizes",
      name: "verbalquizes",
      component: Verbalquizes,
    },
    {
      path: '/VerbalAbilityQuizPage/:quizNumber',
      name: 'VerbalAbilityQuizPage',
      component: VAQuizPage,
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    },
    {
      path: "/:pathMatch(.*)*", // Catch-all route for 404 Not Found
      name: "notfound",
      component: NotFound, // Not Found page component
    },
    {
      path: '/company-specific',
      name: 'company-specific',
      component: CompanySpecific // The new CompanySpecific component
    },
    {
      path: '/barclays',
      name: 'barclays-landing',
      component: BarclaysLanding
    },
    {
      path: '/deutschebank',
      name: 'deutschebank-landing',
      component: DeutscheBankLanding
    },
    {
      path: '/jpmorgan',
      name: 'jpmorgan-landing',
      component: JPMorganLanding
    },
    {
      path: '/accenture',
      name: 'accenture-landing',
      component: AccentureLanding
    },
    {
      path: '/tcs',
      name: 'tcs-landing',
      component: TCSLanding
    },
    {
      path: '/oracle',
      name: 'oracle-landing',
      component: OracleLanding
    },
    {
      path: '/wipro',
      name: 'wipro-landing',
      component: WiproLanding
    },
    {
      path: '/cognizant',
      name: 'cognizant-landing',
      component: CognizantLanding
    },
    {
      path: '/google',
      name: 'google-landing',
      component: GoogleLanding
    },
    {
      path: '/microsoft',
      name: 'microsoft-landing',
      component: MicrosoftLanding
    },
    {
      path: '/amazon',
      name: 'amazon-landing',
      component: AmazonLanding
    },
    {
      path: '/siemens',
      name: 'siemens-landing',
      component: SiemensLanding
    },
    {
      path: '/nvidia',
      name: 'nvidia-landing',
      component: NvidiaLanding
    },
    {
      path: '/deloitte',
      name: 'deloitte-landing',
      component: DeloitteLanding
    },
    {
      path: '/airtel',
      name: 'airtel-landing',
      component: AirtelLanding
    },
    {
      path: '/coding-ide',
      name: 'coding-ide',
      component: CodingIde // Add the route for the Coding IDE
    },
    {
      path: "/barclays/mock-exam",
      name: "mock-exam-page",
      component: MockExamBarclays
      // component: () => import("@/components/MockExamBarclays.vue"),
    },
    // {
    //   path: "/barclays/exam-window",
    //   name: "exam-window",
    //   component: ExamWindowBarclays
    // }
    {
      path: '/automata',
      component: AutomataPage
    },
    
    
    
  ],
});

// Export the router instance
export default router;
