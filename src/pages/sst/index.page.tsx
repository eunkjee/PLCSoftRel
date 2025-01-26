import { useState } from "react";
import Link from "next/link";
import Logo from "@/assets/logo.svg";
import { useRouter } from "next/router";
import axios from "axios";

export default function Index() {
  const router = useRouter();

  // 민감도 분석 상태
  const [pfdGoal, setPfdGoal] = useState('');
  const [confidenceGoal, setConfidenceGoal] = useState('');
  const [numTests, setNumTests] = useState('');

  // PFD 업데이트 상태
  const [tests, setTests] = useState<number>(0);
  const [failures, setFailures] = useState<number>(0);
  const [updatedPfd, setUpdatedPfd] = useState<number | null>(null);
  const [updatedConfidence, setUpdatedConfidence] = useState<number | null>(null);

  const handleSensitivitySubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/sensitivity-analysis', {
        pfd_goal: parseFloat(pfdGoal),
        confidence_goal: parseFloat(confidenceGoal)
      });
      setNumTests(`계산된 테스트 수: ${response.data.data.num_tests}`);
    } catch (error) {
      console.error("Error calling sensitivity analysis API", error);
    }
  };

  const handlePfdUpdateSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await axios.post('http://localhost:8000/api/update-pfd', {
        pfd_goal: 0.0001, // 필요한 목표 값을 지정
        demand: tests,
        failures: failures
      });
      setUpdatedPfd(response.data.data.updated_pfd);
      setUpdatedConfidence(response.data.data.updated_confidence);
    } catch (error) {
      console.error("Error calling update PFD API", error);
    }
  };

  return (
    <>
      <header style={{ padding: '10px', borderBottom: '1px solid #ddd' }}>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <Link href="/">
            <Logo />
          </Link>
          <nav style={{ marginLeft: '20px' }}>
            <button onClick={() => router.push('/')}>Bayesian Methods</button>
            <button onClick={() => router.push('/statistical')}>Statistical Methods</button>
            <button onClick={() => router.push('/reliability')}>Reliability Views</button>
          </nav>
        </div>
      </header>

      <main style={{ padding: '20px', fontFamily: 'Arial, sans-serif' }}>
        <h1>Statistical Methods</h1>

        {/* 민감도 분석 섹션 */}
        <section style={{ marginBottom: '20px', padding: '20px', border: '1px solid #ddd' }}>
          <h2>1. Sensitivity Analysis</h2>
          <form onSubmit={handleSensitivitySubmit}>
            <div>
              <label>
                PFD Goal:
                <input
                  type="text"
                  value={pfdGoal}
                  onChange={(e) => setPfdGoal(e.target.value)}
                  style={{ marginLeft: '10px', marginRight: '20px' }}
                />
              </label>
              <label>
                Confidence Goal:
                <input
                  type="text"
                  value={confidenceGoal}
                  onChange={(e) => setConfidenceGoal(e.target.value)}
                  style={{ marginLeft: '10px' }}
                />
              </label>
              <button type="submit" style={{ marginLeft: '10px' }}>Submit</button>
            </div>
            {numTests && (
              <div style={{ marginTop: '10px' }}>
                <strong>Output - Number of Tests:</strong> {numTests}
              </div>
            )}
          </form>
        </section>

        {/* PFD 업데이트 섹션 */}
        <section style={{ padding: '20px', border: '1px solid #ddd' }}>
          <h2>2. Update PFD</h2>
          <form onSubmit={handlePfdUpdateSubmit}>
            <div>
              <label>
                Number of Tests:
                <input
                  type="number"
                  value={tests}
                  onChange={(e) => setTests(Number(e.target.value))}
                  style={{ marginLeft: '10px', marginRight: '20px' }}
                />
              </label>
              <label>
                Number of Failures:
                <input
                  type="number"
                  value={failures}
                  onChange={(e) => setFailures(Number(e.target.value))}
                  style={{ marginLeft: '10px' }}
                />
              </label>
              <button type="submit" style={{ marginLeft: '10px' }}>Submit</button>
            </div>
            {(updatedPfd !== null && updatedConfidence !== null) && (
              <div style={{ marginTop: '10px' }}>
                <strong>Output - Updated PFD:</strong> {updatedPfd} <br />
                <strong>Output - Updated Confidence Level:</strong> {updatedConfidence}
              </div>
            )}
          </form>
        </section>

        <footer style={{ marginTop: '20px', padding: '10px', fontSize: '14px', color: '#555' }}>
          &lt;&lt;Output에 대한 설명 추가&gt;&gt;
        </footer>
      </main>
    </>
  );
}
