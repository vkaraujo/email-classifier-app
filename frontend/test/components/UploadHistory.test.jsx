import { render, screen, fireEvent } from '@testing-library/react'
import UploadHistory from '../../src/components/UploadHistory'

describe('UploadHistory', () => {
  it('renders nothing if lastResults is empty', () => {
    const { container } = render(<UploadHistory lastResults={[]} onSelectHistory={() => {}} />)
    expect(container.firstChild).toBeNull()
  })

  it('renders a list of items with proper colors', () => {
    const data = [
      { file: "email1.txt", categoria: "Produtivo" },
      { file: "email2.txt", categoria: "Improdutivo" },
      { text: "some inserted text", categoria: "Produtivo" },
    ]

    render(<UploadHistory lastResults={data} onSelectHistory={() => {}} />)

    expect(screen.getByText(/Histórico/i)).toBeInTheDocument()
    expect(screen.getByText(/email1.txt/i)).toBeInTheDocument()
    expect(screen.getByText(/email2.txt/i)).toBeInTheDocument()
    expect(screen.getByText(/Texto inserido/i)).toBeInTheDocument()
  })

  it('calls onSelectHistory when an item is clicked', async () => {
    const data = [
      { file: "email1.txt", categoria: "Produtivo" },
      { file: "email2.txt", categoria: "Improdutivo" },
    ]
    const onSelectHistory = vi.fn()

    render(<UploadHistory lastResults={data} onSelectHistory={onSelectHistory} />)

    const firstItem = screen.getByText(/email1.txt/i)
    await fireEvent.click(firstItem)

    expect(onSelectHistory).toHaveBeenCalledTimes(1)
    expect(onSelectHistory).toHaveBeenCalledWith(expect.objectContaining({ file: "email1.txt" }))
  })
})
