import { render, screen } from '@testing-library/react'
import UploadResult from '../../src/components/UploadResult'

describe('UploadResult', () => {
  it('renders nothing if result is empty', () => {
    const { container } = render(<UploadResult result={[]} highlight={false} />)
    expect(container.firstChild).toBeNull()
  })

  it('renders multiple results with correct categories and suggested responses', () => {
    const mockResults = [
      { file: "email1.txt", categoria: "Produtivo", resposta_sugerida: "Resposta 1" },
      { file: "email2.txt", categoria: "Improdutivo", resposta_sugerida: "Resposta 2" },
      { text: "some text", categoria: "Outro", resposta_sugerida: "Resposta 3" }
    ]

    render(<UploadResult result={mockResults} highlight={false} />)

    expect(screen.getByText(/Arquivo: email1.txt/i)).toBeInTheDocument()
    expect(screen.getAllByText(/Produtivo/i).length).toBeGreaterThan(0)
    expect(screen.getByText(/Resposta 1/i)).toBeInTheDocument()

    expect(screen.getByText(/Arquivo: email2.txt/i)).toBeInTheDocument()
    expect(screen.getByText(/Improdutivo/i)).toBeInTheDocument()
    expect(screen.getByText(/Resposta 2/i)).toBeInTheDocument()

    expect(screen.getByText(/Texto inserido/i)).toBeInTheDocument()
    expect(screen.getByText(/Outro/i)).toBeInTheDocument()
    expect(screen.getByText(/Resposta 3/i)).toBeInTheDocument()
  })

  it('applies highlight class when highlight is true', () => {
    const mockResults = [
      { file: "email1.txt", categoria: "Produtivo", resposta_sugerida: "Resposta 1" },
    ]

    const { container } = render(<UploadResult result={mockResults} highlight={true} />)
    expect(container.firstChild).toHaveClass('bg-blue-100')
  })

  it('applies normal background when highlight is false', () => {
    const mockResults = [
      { file: "email1.txt", categoria: "Produtivo", resposta_sugerida: "Resposta 1" },
    ]

    const { container } = render(<UploadResult result={mockResults} highlight={false} />)
    expect(container.firstChild).toHaveClass('bg-gray-50')
  })
})
